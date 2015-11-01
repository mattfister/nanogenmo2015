import random
from wordtools import wordLists, names
from setting_paragraph import Paragraph
from wordtools import md_writer
from fantasy_novel_state import FantasyNovelState

names = names.Names()
words = wordLists.WordLists()

words = wordLists.WordLists()


def generate_title():
    # TODO: Terrible
    title = 'The ' + words.get_adj().title() + " " + random.choice(["Legend", "Tale", "Story", "Adventure"]) + " of " \
            + random.choice(["Glory", "Heroes", "Ages"])
    md_writer.print_title(title)


def generate_novel():
    generate_title()
    state = FantasyNovelState()

    setting = state.get_current_setting()
    while setting is not None:
        paragraph = Paragraph(state)
        paragraph.generate_sentences()
        setting = state.next_setting()

if __name__ == '__main__':
    generate_novel()
    md_writer.end_novel()
