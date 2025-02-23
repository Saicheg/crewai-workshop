from joke_teller.crew import CreateJokeCrew

if __name__ == '__main__':
    website = input("Enter a website for the joke: ")
    crew = CreateJokeCrew().crew()
    inputs = { "website": website }
    result = crew.kickoff(inputs=inputs)
