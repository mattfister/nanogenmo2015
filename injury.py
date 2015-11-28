from wordtools import md_writer
from wordtools import aOrAn
import random

class Injury:

    def __init__(self, character, cause):
        self.character = character
        self.description = random.choice(["broken rib", "shattered sternum", "broken leg",
                                          "bruised face", "broken arm", "broken nose",
                                          "concussion", "herniated disc", "bruised skull",
                                          "shattered elbow", "injured spine", "sliced hamstring",
                                          "torn spleen", "pierced guts"])

        if (cause == None):
            md_writer.print_chapter_sentence(character.get_description().title() + " was injured with " + aOrAn(self.description) + " " + self.description + ".")
        else:
            md_writer.print_chapter_sentence(cause.get_description().title() + "'s attack caused " + self.character.get_description() + " to have " + aOrAn.aOrAn(self.description) + " " + self.description + ".")

    def get_description(self):
        return self.description

