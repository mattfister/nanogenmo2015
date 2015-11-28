from wordtools import md_writer
from wordtools import wordLists
import random

words = wordLists.WordLists()

class FinalChapter():

    def __init__(self, state):
        self.state = state

    def first_sentence(self):
        sentence = ''
        cs = self.state.get_characters()
        random.shuffle(cs)
        for i in range(len(cs)):
            sentence += cs[i].get_name()
            if i < len(cs) - 2:
                sentence += ', '
            elif i == len(cs) - 2:
                sentence += ', and '
            else:
                sentence += ' finally arrived at '+ self.state.goal_setting_name + "."
        return sentence

    def write_chapter(self):
        md_writer.print_chapter_heading(self.state.goal_setting_name)
        md_writer.print_chapter_sentence(self.first_sentence())
        c = random.choice(self.state.get_characters())
        md_writer.print_chapter_sentence(c.get_description() + " threw " + self.state.macguffin_name + " into the burning void.")
        md_writer.print_chapter_sentence("Suddenly, the powerful wizard, " + self.state.wizard_name + " appeared in a flash of light.")
        md_writer.print_chapter_sentence(self.state.wizard_name + " said, " + '"You have saved the world! It was a terrible journey but you did it!"')
        md_writer.end_chapter()
