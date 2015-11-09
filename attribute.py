import random

class Attribute():

    def __init__(self, name):
        self.name = name
        self.value = random.randint(1, 6) + random.randint(1, 6)

    def challenge(self):
        return self.value < random.randint(1, 6) + random.randint(1, 6)
