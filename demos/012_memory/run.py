from joke_teller.crew import CreateJokeCrew
from mem0 import MemoryClient

client = MemoryClient()

if __name__ == '__main__':
    messages = []
    user = "valentine"

    while True:
        topic = input("Enter a topic for the joke: ")

        crew = CreateJokeCrew(user).crew()
        inputs = { "topic": topic }
        response = crew.kickoff(inputs=inputs)

        feedback = input("Do you like the joke: ")

        messages = [
            {"role": "assistant", "content": "Enter a topic for the joke: "},
            {"role": "user", "content": topic},
            {"role": "assistant", "content": response.raw},
            {"role": "assistant", "content": "How do you liked a joke?"},
            {"role": "user", "content": feedback},
        ]
        client.add(messages, user_id=user)
