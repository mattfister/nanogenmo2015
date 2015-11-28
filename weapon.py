import random

class Weapon:
    def __init__(self):
        self.name = random.choice(['dagger', 'short sword', 'claymore', 'battleaxe', 'morningstar',
                                   'mace', 'warhammer', 'staff', 'long sword', 'halberd', 'club'])

    def get_name(self):
        return self.name

    def get_description(self):
        return self.get_name()
