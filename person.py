import random
from wordtools import wordLists, names
from wordtools import conceptnet_searcher

names = names.Names()
words = wordLists.WordLists()


def generate_quality():
    while True:
        quality = words.get_living_thing_adj()
        try: 
            conceptnet_searcher.get_concept_relations(quality)
            return quality
        except Exception:
            continue

class Person:
    
    def __init__(self):
        self.full_name = names.get(random.choice(["male", "female"]))

        self.first_name = self.full_name.split(' ')[0]
        if len(self.full_name.split(' ')[0]) > 1:
            self.last_name  = self.full_name.split(' ')[1]
            
        else:
            self.last_name = ""

        self.qualities = (generate_quality(), generate_quality(), generate_quality())
        self.history = []

    def add_history(happening):
        self.history.append(happening)

