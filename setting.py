from wordtools import wordLists
from wordtools import conceptnet_searcher
from wordtools import aOrAn
from wordtools import old_language_generator
import random

words = wordLists.WordLists()


class Setting:

    def generate_setting(self):
        return words.get_fantasy_place()
        while True:
            setting = words.get_fantasy_place()
            try:
                print setting
                conceptnet_searcher.get_concept_relations(setting)
                return setting
            except Exception:
                continue

    def __init__(self):
        self.name = self.generate_setting()

        self.adjective = words.get_place_adj()

        self.props = [i[1].replace('_', ' ') for i in conceptnet_searcher.get_concept_relations(self.name) if i[0] == 'HasA']

        for i in range(2):
            self.props.append(words.get_fantasy_prop())

        random.shuffle(self.props)
        self.props = self.props[:2]

        print self.props

        self.old_name = (old_language_generator.translate_word(self.name) + ' ' + old_language_generator.random_word()).title()
        self.known_props = []

        self.race = words.get_fantasy_race()

        self.occupation = words.get_fantasy_occupation()

        self.danger = random.choice(['very dangerous', 'dangerous', 'safe'])

        self.lore_facts = ["This place was once known as *" + self.old_name + "*",
                           self.race.title() + " " + self.occupation + " once ruled this place",
                           "This is a " + self.danger + " " + random.choice(["place", self.name])]
        random.shuffle(self.lore_facts)

    def has_more_lore(self):
        return len(self.lore_facts) > 0

    def discover_lore(self):
        return self.lore_facts.pop()

    def get_name(self):
        return self.name

    def get_description(self):
        return random.choice([self.name, self.adjective + ' ' + self.name])

    def get_old_name(self):
        return self.old_name

    def get_props(self):
        return self.props

    def get_known_props(self):
        return self.known_props

    def discover_prop(self, char, prop, setting):
        self.props.remove(prop)
        self.known_props.append(prop)
        if char != None:
            return char + " " + random.choice(["discovered", "found", "noticed"]) + " " + aOrAn.aOrAn(prop) + " " + prop + " inside the " + setting + "."
        else:
            return "There was " + aOrAn.aOrAn(prop) + " " + prop + " inside the " + setting + "."

    def mood_sentence(self):
        return random.choice(['The wind blew gently through the ' + self.get_name() + '.',
                              'A rustling sound was heard in the distance.',
                              'A sudden chill fell over the ' + self.get_name() + '.',
                              'The ' + self.get_name() + ' seemed more sinister all of a sudden.'])
