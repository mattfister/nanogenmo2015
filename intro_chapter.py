from wordtools import md_writer
from wordtools import wordLists
from wordtools import old_language_generator
import random

words = wordLists.WordLists()

class IntroChapter():

    def __init__(self, state):
        self.state = state

        self.inn_name = "The " + random.choice(['Red', 'Blue', 'Black', 'Shining',
                                                'Odd', 'Great', 'Greater', 'Strange',
                                                'Cozy']) + " " + random.choice(['Inn', 'Flagon', 'Tankard',
                                                'Sheep', 'Hog', 'Cup']) + " Inn"

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
                sentence += ' were drinking at ' + self.inn_name + '.'
        return sentence

    def write_chapter(self):
        md_writer.print_chapter_heading(self.inn_name)
        md_writer.print_chapter_sentence(self.first_sentence())
        md_writer.print_chapter_sentence("Suddenly, the powerful wizard, " + self.state.wizard_name + " appeared in a flash of light.")
        md_writer.print_chapter_sentence(self.state.wizard_name + " said, " + '"You must take ' + self.state.macguffin_name + ' to ' + self.state.goal_setting_name + ' and destroy it, or the world will end! Many agents of chaos will oppose you, but only you can save the world!"')
        c = random.choice(self.state.get_characters())
        md_writer.print_chapter_sentence(c.get_description() + " took " + self.state.macguffin_name + ", and the three heroes went off.")
        md_writer.end_chapter()
