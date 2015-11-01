import random
from wordtools import wordLists, names
from setting_paragraph import Paragraph
from person import Person
from wordtools import conceptnet_searcher

import sys
from wordtools import md_writer

names = names.Names()
words = wordLists.WordLists()

words = wordLists.WordLists()

def generate_character():
    choice = random.random()
    if choice < 0.9:
        return names.get(random.choice(["male", "female"]))
    else:
        return words.get_celeb()

def generate_setting():
    while True:
        setting = words.get_fantasy_place()
        try:
            print setting
            conceptnet_searcher.get_concept_relations(setting)
            return setting
        except Exception:
            print sys.exc_info()[0]
            continue

def generate_title():
    title = 'The ' + words.get_adj().title() + " " + random.choice(["Legend", "Tale", "Story", "Adventure"]) + " of " \
            + random.choice(["Glory", "Heroes", "Ages"])
    md_writer.print_title(title)

def generate_novel():
    generate_title()
    characters = [Person(), Person(), Person()]
    for i in range(30):
        setting = generate_setting()
        paragraph = Paragraph(characters, setting)
        paragraph.generate_sentences()

if __name__ == '__main__':
    generate_novel()
    md_writer.end_novel()
