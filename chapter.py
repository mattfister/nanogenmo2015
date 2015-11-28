from wordtools import wordLists
from wordtools import md_writer
from setting_paragraph import SettingParagraph
from food_paragraph import FoodParagraph
from camp_paragraph import CampParagraph
from combat_paragraph import CombatParagraph
import string
import random

words = wordLists.WordLists()


class Chapter:
    def __init__(self, state):
        self.state = state
        self.paragraphs = []
        self.paragraphs.append(SettingParagraph(self.state))
        food_r = random.random()
        extra_paragraphs = []
        self.potential_titles = []
        self.potential_titles.append('The ' + string.capwords(self.state.get_current_setting().get_description()))

        if (self.state.get_food_level() == 'medium' and food_r < 0.1) or \
            (self.state.get_food_level() == 'low' and food_r < 0.3) or \
            (self.state.get_food_level() == 'none' and food_r < 0.5):
            food_paragraph = FoodParagraph(self.state)
            extra_paragraphs.append(food_paragraph)
            self.potential_titles.append(food_paragraph.method.title() + ' In The ' + string.capwords(self.state.get_current_setting().get_name()))

        energy_r = random.random()
        if (self.state.get_energy_level() == 'medium' and energy_r < 0.1) or \
            (self.state.get_energy_level() == 'low' and energy_r < 0.3) or \
            (self.state.get_energy_level() == 'none' and energy_r < 0.5):
            self.potential_titles.append('Camping' + ' In The ' + string.capwords(self.state.get_current_setting().get_description()))
            extra_paragraphs.append(CampParagraph(self.state))

        if len(self.state.get_enemy_patrols()) > 0 and random.random() > 0.5:
            self.potential_titles.append('The Battle In The ' + string.capwords(self.state.get_current_setting().get_description()))
            extra_paragraphs.append(CombatParagraph(self.state))

        random.shuffle(extra_paragraphs)
        self.paragraphs += extra_paragraphs

    def write_chapter(self):
        md_writer.print_chapter_heading(random.choice(self.potential_titles))
        for paragraph in self.paragraphs:
            paragraph.generate_sentences()
            md_writer.end_paragraph()
