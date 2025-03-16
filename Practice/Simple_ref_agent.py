class RoomCleaner:
    def __init__(self):
        self.location = "Room1"
        self.environment = {
            "Room1":"Dirty",
            "Room2":"Dirty"          
        }
    
    def perceive(self):
        return self.environment[self.location]
    
    def clean(self):
        if self.perceive() == "Dirty":
            print(f"Cleaning the {self.location}")
            self.environment[self.location] = "Clean"
        else:
            print(f"{self.location} is cleaned. Moving towards the next room.")
            if self.location == "Room1":
                self.location = "Room2"
            else:
                self.location = "Room1"
    
    def run_cleaner(self, steps = 2):
        for _ in range(steps):
            self.clean()
    
room_cleaner = RoomCleaner()

room_cleaner.run_cleaner(4)
