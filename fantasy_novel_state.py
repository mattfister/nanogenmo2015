from person import Person
from wordtools import wordLists
from setting import Setting
from says_sentence import says_sentence
from npc import Npc
from wordtools import old_language_generator
import random
words = wordLists.WordLists()


class FantasyNovelState:

    def __init__(self):
        self.characters = [Person(), Person(), Person()]

        self.setting_map = []
        self.setting_map_location = 0
        for i in range(325):
            self.setting_map.append(Setting())

        self.food = random.randint(6, 12)
        self.energy = random.randint(6, 20)
        self.enemy_patrols = []

        self.wizard_name = old_language_generator.random_word().title() + " The " + words.get_living_thing_adj().title()

        self.macguffin_name = "The " + words.get_adj().title() + " " + words.get_fantasy_prop().title()

        self.goal_setting_name = "The " + words.get_place_adj().title() + random.choice([" Volcano", " Chasm", " Geyser" " Abyss"])


    def get_enemy_patrols(self):
        return self.enemy_patrols

    def get_characters(self):
        return self.characters

    def get_current_setting(self):
        return self.setting_map[self.setting_map_location]

    def next_setting(self):
        self.setting_map_location += 1
        self.food -= 1
        self.energy -= 1
        if self.setting_map_location < len(self.setting_map) - 1:
            return self.setting_map[self.setting_map_location]
        else:
            return None

    def level(self, quantity):
        if quantity >= 8:
            return 'high'
        elif quantity >= 3:
            return 'medium'
        elif quantity >= 1:
            return 'low'
        else:
            return 'none'

    def get_food_level(self):
        return self.level(self.food)

    def get_energy_level(self):
        return self.level(self.energy)

    def add_enemy_patrol(self, race):
        new_enemies = [Npc(race), Npc(race)]
        self.enemy_patrols.append(new_enemies)

    def generate_injury_sentence(self, c):
        if len(c.get_injuries()) > 0:
            injury = random.choice(c.get_injuries())
            return says_sentence(c, 'My ' + injury.get_description() + ' hurts')
        else:
            return self.get_current_setting().mood_sentence()

    def generate_enemy_sentence(self, c):
        followed_sentences = ['I just heard something move',
                              "I think we are being followed",
                              "I have a bad feeling",
                              "I saw something move",
                              "I thought I saw something over there"]
        not_followed_sentences = ["It's so peaceful here",
                                  "It is so quiet",
                                  "I think we're alone",
                                  "It's very quiet here"]
        if len(self.enemy_patrols) > 0:
            return says_sentence(c, random.choice(followed_sentences))
        else:
            return says_sentence(c, random.choice(not_followed_sentences))

    def generate_food_sentence(self, c):
        high_food_sentences = ['We have a lot of food',
                               'Our supplies should last a while',
                               'We have food for many days',
                               "Let's continue, we don't have to worry about food",
                               "We are well supplied"]
        medium_food_sentences = ["Our food should last a bit longer",
                                 "We have food to last several days",
                                 "Our supplies are in decent shape",
                                 "We have a good amount of food"]
        low_food_sentences = ["We are running low on food",
                              "We should consider searching for supplies",
                              "We're running out of supplies",
                              "Our food will last only a few more days"]
        no_food_sentences = ["Our food is all gone",
                             "We're out of food",
                             "Our supplies have run out",
                             "We need to hunt for food",
                             "I'm starving"]

        if self.level(self.food) == 'high':
            return says_sentence(c, random.choice(high_food_sentences))
        elif self.level(self.food) == 'medium':
            return says_sentence(c, random.choice(medium_food_sentences))
        elif self.level(self.food) == 'low':
            return says_sentence(c, random.choice(low_food_sentences))
        else:
            return says_sentence(c, random.choice(no_food_sentences))

    def generate_energy_sentence(self, c):
        high_energy_sentences = ['',
                               'We should keep moving, before we get tired',
                               'I feel refreshed',
                               "I feel energized",
                               "Let's hurry"]
        medium_energy_sentences = ["Let's keep moving",
                                 "I'm not tired yet",
                                 "We should keep going for a while",
                                 "Let's not camp yet"]
        low_energy_sentences = ["I'm getting tired",
                              "We should make camp soon",
                              "You're looking tired",
                              "I'm feeling rather sleepy"]
        no_energy_sentences = ["I'm exhausted",
                             "Let's make camp now",
                             "We should find a suitable place to camp",
                             "Let's take a break",
                             "Argh! I'm so tired"]

        if self.level(self.energy) == 'high':
            return says_sentence(c, random.choice(high_energy_sentences))
        elif self.level(self.energy) == 'medium':
            return says_sentence(c, random.choice(medium_energy_sentences))
        elif self.level(self.food) == 'low':
            return says_sentence(c, random.choice(low_energy_sentences))
        else:
            return says_sentence(c, random.choice(no_energy_sentences))

    def generate_status_sentence(self):
        sentence_to_gen = random.choice([self.generate_food_sentence,
                                         self.generate_energy_sentence,
                                         self.generate_enemy_sentence,
                                         self.generate_injury_sentence])

        return sentence_to_gen(random.choice(self.characters))

    def add_food(self, food):
        self.food += food

    def add_energy(self, energy):
        self.energy += energy

    def character_list(self):
        sentence = ""
        cs = self.get_characters()
        random.shuffle(cs)
        for i in range(len(cs)):
            sentence += cs[i].get_name()
            if i < len(cs) - 2:
                sentence += ', '
            elif i == len(cs) - 2:
                sentence += ', and '
        return sentence

    def dequeue_enemy_patrol(self):
        return self.enemy_patrols.pop(0)