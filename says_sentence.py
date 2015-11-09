import random


def says_sentence(character, subject):
    said_word = random.choice(['announced', 'mentioned', 'uttered', 'stated',
                               'exclaimed', 'proclaimed', 'cried out'])
    return character.get_name() + " " + said_word + ', "' + subject + '."'

