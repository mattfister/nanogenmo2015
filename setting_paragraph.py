import generate_concept_sentence
from wordtools import conceptnet_searcher
import random
from wordtools import wordLists
from wordtools import aOrAn
from wordtools import md_writer


class Paragraph:

    def __init__(self, state):
        self.state = state
        self.words = wordLists.WordLists()

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

    def generate_sentences(self):
        md_writer.print_chapter_sentence(self.setting_sentence(self.state))

        for i in range(10):
            if random.random() < 0.5:
                md_writer.print_chapter_sentence(generate_concept_sentence.generate_concept_sentence(random.choice((random.choice(self.state.get_characters()).first_name, None)), self.state.get_current_setting().get_name()))
            else:
                if len(self.state.get_current_setting().get_props()) > 0:
                    md_writer.print_chapter_sentence(self.state.get_current_setting().discover_prop(random.choice((random.choice(self.state.get_characters()).first_name, None)), random.choice(self.state.get_current_setting().get_props()), self.state.get_current_setting().get_name()))
                elif len(self.state.get_current_setting().get_known_props()) > 0:
                    try:
                        print md_writer.print_chapter_sentence(generate_concept_sentence.generate_concept_sentence(random.choice((random.choice(self.state.get_characters()).first_name, None)), random.choice(self.state.get_current_setting().get_known_props())))
                    except Exception:
                        continue

        md_writer.end_chapter()