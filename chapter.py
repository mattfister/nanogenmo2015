__author__ = 'supergork'

from wordtools import wordLists
from wordtools import md_writer
from setting_paragraph import SettingParagraph
from food_paragraph import FoodParagraph
import string
import random

words = wordLists.WordLists()


class Chapter:
    def __init__(self, state):
        self.state = state
        self.paragraphs = []
        self.paragraphs.append(SettingParagraph(self.state))
        food_r = random.random()
        if (self.state.get_food_level() == 'medium' and food_r < 0.1) or \
            (self.state.get_food_level() == 'low' and food_r < 0.3) or \
            (self.state.get_food_level() == 'none' and food_r < 0.5):
            self.paragraphs.append(FoodParagraph(self.state))

    def write_chapter(self):
        md_writer.print_chapter_heading('The ' + string.capwords(self.state.get_current_setting().get_name()))
        for paragraph in self.paragraphs:
            paragraph.generate_sentences()
            md_writer.end_paragraph()
