from person import Person
from wordtools import wordLists
from setting import Setting
words = wordLists.WordLists()


class FantasyNovelState:

    def __init__(self):
        self.characters = [Person(), Person(), Person()]

        self.setting_map = []
        self.setting_map_location = 0
        for i in range(30):
            self.setting_map.append(Setting())

    def get_characters(self):
        return self.characters

    def get_current_setting(self):
        return self.setting_map[self.setting_map_location]

    def next_setting(self):
        self.setting_map_location += 1
        if self.setting_map_location < len(self.setting_map) - 1:
            return self.setting_map[self.setting_map_location]
        else:
            return None
