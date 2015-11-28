from wordtools import names
from wordtools import wordLists
import random
from weapon import Weapon
from injury import Injury
from wordtools import md_writer
from wordtools import aOrAn
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

        self.full_name = names.get(self.gender)

        self.first_name = self.full_name.split(' ')[0]
        if len(self.full_name.split(' ')[0]) > 1:
            self.last_name = self.full_name.split(' ')[1]

        else:
            self.last_name = ""

        self.characteristic = self.generate_characteristic()

        self.weapon = Weapon()

        self.injuries = []

        self.dead = False

    def generate_characteristic(self):
        racial_characteristics = {'elf': ['pierced pointed ear', 'flowing white robe', 'beautiful circlet',
                                          'unusual gait', 'magical aura'],
                                  'orc': ['scarred green face', 'muscular physique', 'leather harness',
                                          'missing tooth', 'bloodstained shirt', 'tangled, greasy mop of hair'],
                                  'dwarf': ['drunken demeanor', 'rotund appearance', 'long beige beard',
                                            'curled mustache', 'golden crown', 'silver amulet', 'flagon of ale'],
                                  'golem': ['brassy sheen', 'silver sheen', 'stone face', 'hideous carved rune',
                                            'blackened limb', 'jerky disposition'],
                                  'kobold': ['barking cough', 'tattered gown', 'yappy voice' 'third eye',
                                             'sharpened claw', 'small cap', 'nervous way of moving'],
                                  'gnome': ['clockwork eyeball', 'pointy hat', 'bulbous nose', 'disgusting pimple',
                                            'insightful gaze']}
        generic_characteristics = ['burly chest', 'asthmatic wheeze', 'hirsute arm', 'angry grimace', 'gray hair',
                                   'kind face', 'sickly pate', 'dusty burlap shirt', 'soft face']

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

    def add_injury(self, cause):
        if len(self.injuries) < 1:
            self.injuries.append(Injury(self, cause))
        else:
            self.dead = True
            if cause != None:
                md_writer.print_chapter_sentence(cause.get_description().title() + " struck " + self.get_description() + " killing " + self.possessive_pronoun + ".")
            else:
                md_writer.print_chapter_sentence(self.get_description().title() + " died.")

    def get_weapon(self):
        return self.weapon

    def is_dead(self):
        return self.dead

    def get_pronoun(self):
        return self.pronoun

    def get_possessive_pronoun(self):
        return self.possessive_pronoun

if __name__ == '__main__':
    npc = Npc(words.get_fantasy_race())
    print npc.get_description()