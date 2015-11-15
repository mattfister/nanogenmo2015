import random

class Weapon:
    def __init__(self):
        self.name = random.choice(['dagger', 'short sword', 'claymore', 'battleaxe', 'morningstart',
                                   'mace', 'warhammer', 'staff', 'long sword'])

    def get_name(self):
        return self.name

