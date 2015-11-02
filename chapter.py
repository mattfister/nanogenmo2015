__author__ = 'supergork'

from wordtools import wordLists
from wordtools import md_writer
from setting_paragraph import Paragraph
import string

words = wordLists.WordLists()


class Chapter:
    def __init__(self, state):
        self.state = state
        self.paragraphs = []
        for i in range(1):
            self.paragraphs.append(Paragraph(self.state))

    def write_chapter(self):
        md_writer.print_chapter_heading('The ' + string.capwords(self.state.get_current_setting().get_name()))
        for paragraph in self.paragraphs:
            paragraph.generate_sentences()
