from agent import Agent


class Mouth(Agent):
    """The speaking agent of the program"""

    def __init__(self):
        """default constructor"""
        super(Mouth, self).__init__("mouth")

    def speak(self):
        message = self.ask("brain", "message")
        print(message)
        

