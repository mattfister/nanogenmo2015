from wordtools import wordLists
from wordtools import conceptnet_searcher
from wordtools import aOrAn
import random

words = wordLists.WordLists()


class Setting:

    def generate_setting(self):
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

        self.props = [i[1].replace('_', ' ') for i in conceptnet_searcher.get_concept_relations(self.name) if i[0] == 'HasA']

        for i in range(2):
            self.props.append(words.get_fantasy_prop())

        random.shuffle(self.props)
        self.props = self.props[:2]

        print self.props

        self.known_props = []

    def get_name(self):
        return self.name

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

