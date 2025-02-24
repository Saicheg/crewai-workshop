from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from joke_with_explanation import JokeWithExplanation
from videos_information import VideosInformation
from .tools import YouTubeSearchToolWrapper
from crewai.tasks.task_output import TaskOutput
from crewai.tasks.conditional_task import ConditionalTask
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

def not_enough_information(output: TaskOutput) -> bool:
    information = output.pydantic
    if len(information.videos) < 5:
        return True
    return False

@CrewBase
class CreateJokeCrew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def channel_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['channel_researcher'],
            tools=[YouTubeSearchToolWrapper()],
        )

    @agent
    def videos_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['videos_researcher'],
            tools=[ScrapeWebsiteTool()],
        )

    @agent
    def google_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['google_researcher'],
            tools=[SerperDevTool()],
        )

    @agent
    def comedian_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['comedian'],
        )

    @task
    def find_latest_videos(self) -> Task:
        return Task(
            config=self.tasks_config['find_latest_videos'],
            agent=self.channel_researcher(),
        )

    @task
    def fetch_videos_information(self) -> Task:
        return Task(
            config=self.tasks_config['fetch_videos_information'],
            agent=self.videos_researcher(),
            output_pydantic=VideosInformation
        )

    @task
    def add_additiona_information(self) -> Task:
        return ConditionalTask(
            config=self.tasks_config['research_channel'],
            agent=self.google_researcher(),
            condition=not_enough_information,
        )

    @task
    def create_joke_task(self) -> Task:
        return Task(
            config=self.tasks_config['create_joke'],
            agent=self.comedian_agent(),
            output_pydantic=JokeWithExplanation,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=True,
        )
