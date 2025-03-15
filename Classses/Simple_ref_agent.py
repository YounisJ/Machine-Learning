class SimpleReflexAgent:
    def __init__(self):
        self.location = "A"  # Agent starts in Room A
        self.environment = {"A": "Dirty", "B": "Dirty"}  # Initial environment

    def perceive(self):
        """Returns the state of the current location."""
        return self.environment[self.location]

    def act(self):
        """Performs an action based on the current perception."""
        if self.perceive() == "Dirty":
            print(f"Cleaning Room {self.location}...")
            self.environment[self.location] = "Clean"
        else:
            print(f"Moving from Room {self.location}...")
            if self.location == "A":
                self.location = "B"
            else:
                self.location = "A"

    def run(self, steps=2):
        """Runs the agent for a fixed number of steps."""
        for _ in range(steps):
            self.act()

# Run the agent
agent = SimpleReflexAgent()
agent.run(4)  # Running for 4 steps
