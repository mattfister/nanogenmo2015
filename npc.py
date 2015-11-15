from wordtools import names
from wordtools import wordLists
import random
from weapon import Weapon

names = names.Names()
words = wordLists.WordLists()

class Npc:

    def __init__(self, race):
        # race is one of [elf, orc, dwarf, golem, kobld, gnome or human]
        self.race = race
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

        self.characteristic = self.generate_characteristic()

        self.weapon = Weapon()

    def generate_characteristic(self):
        racial_characteristics = {'elf': ['pierced pointed ears', 'flowing white robe', 'beautiful circlet',
                                          'unusual gait', 'glowing blue eyes', 'magical aura'],
                                  'orc': ['scarred green skin', 'muscular physique', 'leather harness',
                                          'dreadful teeth', 'bloodstained shirt', 'tangled, greasy hair'],
                                  'dwarf': ['drunken demeanor', 'rotund appearance', 'long beige beard',
                                            'curled mustache', 'golden crown', 'silver amulet', 'flagon of ale'],
                                  'golem': ['brassy sheen', 'silver plating', 'stone face', 'hideous carved runes',
                                            'blackened limbs', 'jerky movements'],
                                  'kobold': ['barking cough', 'tattered gown', 'tiny teeth', 'third eye',
                                             'sharpened claws', 'small cap', 'nervous movements'],
                                  'gnome': ['clockwork eyeball', 'pointy hat', 'bulbous nose', 'disgusting acne',
                                            'insightful gaze']}
        generic_characteristics = ['burly chest', 'asthmatic wheeze', 'hirsute arms', 'angry grimace', 'gray hair',
                                   'puppy dog eyes', 'sickly pate', 'dusty clothes', 'soft face']

        possible_characteristics = generic_characteristics
        if self.race in racial_characteristics.keys():
            possible_characteristics += racial_characteristics[self.race]

        return random.choice(possible_characteristics)

    def get_description(self):
        return 'the ' + self.race + ' with the ' + self.characteristic

    def says(self, subject):
        said_word = random.choice(['announced', 'mentioned', 'uttered', 'stated',
                                   'exclaimed', 'proclaimed', 'cried out'])
        return self.get_description() + " " + said_word + ', "' + subject + '."'

if __name__ == '__main__':
    npc = Npc(words.get_fantasy_race())
    print npc.get_description()