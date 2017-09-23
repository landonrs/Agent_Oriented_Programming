from agent import Agent
from mouth import Mouth
import os


class Brain(Agent):
    """The driver Agent of the program, manages all other agents"""

    def __init__(self):
        """default constructor"""
        super(Brain, self).__init__("brain")

