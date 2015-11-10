import random
from wordtools import wordLists, names
from wordtools import conceptnet_searcher
from attribute import Attribute
from wordtools import md_writer

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
        self.gender = random.choice("male" "female")
        self.possessive_pronoun = 'her'
        self.pronoun = 'she'

        if self.gender == 'male':
            self.possessive_pronoun = 'his'
            self.pronoun = 'he'

        self.full_name = names.get(random.choice(["male", "female"]))

        self.first_name = self.full_name.split(' ')[0]
        if len(self.full_name.split(' ')[0]) > 1:
            self.last_name = self.full_name.split(' ')[1]
            
        else:
            self.last_name = ""

        self.qualities = [generate_quality()]
        self.history = []

        self.attributes = {'combat': Attribute('combat'),
                           'lore': Attribute('lore'),
                           'survival': Attribute('survival')}

        self.memories = {}
        for i in range(5):
            topic = random.choice(['traveling', 'camping', 'hunting', 'fishing' 'searching for food', 'fighting'])
            relation = random.choice(['father', 'mother', 'sister', 'brother', 'best friend', 'rival'])
            when = random.choice(['as a child', 'when ' + self.pronoun + ' was a teenager', 'after leaving ' + self.possessive_pronoun + ' home'])
            self.add_memory(topic, self.get_name() + ' remembered ' + topic + ' with ' + self.possessive_pronoun + ' ' + relation + ' ' + when + '.')

    def get_pronoun(self):
        return self.pronoun

    def get_possessive_pronoun(self):
        return self.possessive_pronoun

    def add_memory(self, topic, sentence):
        try:
            self.memories[topic].append(sentence)
        except KeyError:
            self.memories[topic] = [sentence]

    def get_memory(self, topic):
        try:
            return random.choice(self.memories[topic])
        except KeyError:
            return None

    def add_history(self, happening):
        self.history.append(happening)

    def get_name(self):
        return random.choice([self.full_name, self.first_name, self.first_name + ' the ' + random.choice(self.qualities)]);

    def get_attribute(self, attribute_name):
        return self.attributes[attribute_name]

    def challenge(self, attribute_name):
        return self.get_attribute(attribute_name).challenge()

    def set_positive_quality(self):
        new_quality = words.get_positive_quality()
        md_writer.print_chapter_sentence('Because of this great accomplishment ' + self.get_name() + " became known as 'The " + new_quality.title()+"'.")
        self.qualities = [new_quality]

    def set_negative_quality(self):
        new_quality = words.get_negative_quality()
        md_writer.print_chapter_sentence('Because of this great failure ' + self.get_name() + " became known as 'The " + new_quality.title()+"'.")
        self.qualities = [new_quality]
