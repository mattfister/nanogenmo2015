import generate_concept_sentence
import random
from wordtools import wordLists
from wordtools import md_writer
from says_sentence import says_sentence
from paragraph import Paragraph

lore_fail_exclamations = ['I have never heard of this place',
                          'This place is frightening me',
                          'We should leave this place at once',
                          'I am horrified at the thought of being here',
                          'I have never seen a place like this',
                          'I hate this place',
                          "Let's get out of here",
                          "I don't like the looks of this place",
                          "Let's move on",
                          "I don't think we should stick around here",
                          "This place is a mystery to me",
                          "Let's keep moving"]


class SettingParagraph(Paragraph):

    def __init__(self, state):
        super(SettingParagraph, self).__init__(state)

    def setting_sentence(self, state):
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
                sentence += ' traveled to a ' + self.state.get_current_setting().get_name() + '.'
        return sentence

    def generate_lore_sentence(self, state):
        c = random.choice(self.state.get_characters())
        if c.challenge('lore'):
            return says_sentence(c, self.state.get_current_setting().discover_lore())
        else:
            return says_sentence(c, random.choice(lore_fail_exclamations))

    def generate_sentences(self):
        md_writer.print_chapter_sentence(self.setting_sentence(self.state))

        for i in range(10):
            r = random.random()
            if r < 0.1 and self.state.get_current_setting().has_more_lore():
                md_writer.print_chapter_sentence(self.generate_lore_sentence(self.state))
            elif r < 0.2:
                md_writer.print_chapter_sentence(self.state.generate_status_sentence())
            elif r < 0.5:
                md_writer.print_chapter_sentence(generate_concept_sentence.generate_concept_sentence(random.choice((random.choice(self.state.get_characters()).first_name, None)), self.state.get_current_setting().get_name()))
            else:
                if len(self.state.get_current_setting().get_props()) > 0:
                    md_writer.print_chapter_sentence(self.state.get_current_setting().discover_prop(random.choice((random.choice(self.state.get_characters()).first_name, None)), random.choice(self.state.get_current_setting().get_props()), self.state.get_current_setting().get_name()))
                elif len(self.state.get_current_setting().get_known_props()) > 0:
                    try:
                        print md_writer.print_chapter_sentence(generate_concept_sentence.generate_concept_sentence(random.choice((random.choice(self.state.get_characters()).first_name, None)), random.choice(self.state.get_current_setting().get_known_props())))
                    except Exception:
                        continue
