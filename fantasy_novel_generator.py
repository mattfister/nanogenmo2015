import random
from wordtools import wordLists, names
from chapter import Chapter
from wordtools import md_writer
from fantasy_novel_state import FantasyNovelState
from intro_chapter import IntroChapter
from final_chapter import FinalChapter

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

    intro = IntroChapter(state)
    intro.write_chapter()

    while setting is not None:
        chapter = Chapter(state)
        chapter.write_chapter()
        setting = state.next_setting()

    ending = FinalChapter(state)
    ending.write_chapter()
    md_writer.end_novel()

if __name__ == '__main__':
    generate_novel()
