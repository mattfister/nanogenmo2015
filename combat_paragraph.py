from paragraph import Paragraph
from wordtools import md_writer
from wordtools import num2words
from injury import Injury
from wordtools import aOrAn
from npc import Npc
import random
import pattern.en
import copy


class CombatParagraph(Paragraph):

    def __init__(self, state):
        super(CombatParagraph, self).__init__(state)
        self.patrol = self.state.dequeue_enemy_patrol()

    def living_npc(self):
        living_enemies = []
        for npc in self.patrol:
            if npc.is_dead() == False:
                living_enemies.append(npc)
        return random.choice(living_enemies)

    def hit_sentence(self, c1, c2):
        return c1.get_description().title() + ' struck the ' + c2.get_description() + " with " + c1.get_possessive_pronoun() + ' ' + c1.get_weapon().get_description() + "."

    def miss_sentence(self, c1, c2):
        r = random.random()
        if r < 0.1:
            return c1.get_description().title() + ' tried to strike the ' + c2.get_description() + " with " + c1.get_possessive_pronoun() + ' ' + c1.get_weapon().get_description() + ", but " + c2.get_description() + " dodged the attack."
        elif r < 0.2:
            return c1.get_description().title() + ' circled around ' + c2.get_description() + ', looking for an opening.'
        elif r < 0.3:
            return c1.get_description().title() + ' grunted wearily.'
        elif r < 0.4:
            return c1.get_description().title() + ' stumbled.'
        elif r < 0.5:
            return c1.get_description().title() + ' clutched ' + c1.get_possessive_pronoun() + ' ' + c1.get_weapon().get_description() + '.'
        elif r < 0.6:
            return c2.get_description().title() + ' leapt away from ' + c1.get_description().title() + '.'
        elif r < 0.7:
            return c2.get_description().title() + ' parried ' + c1.get_description().title() + "'s " + c1.get_weapon().get_description() + ' with ' + c2.get_possessive_pronoun() + ' ' + c2.get_weapon().get_description() + '.'
        else:
            return self.state.get_current_setting().mood_sentence()

    def generate_sentences(self):
        race = self.patrol[0].race
        number = num2words.numToWords(len(self.patrol))
        md_writer.print_chapter_sentence("Suddenly " + number + " " + pattern.en.pluralize(race) + " ambushed the group.")

        done = False

        while not done:
            done = True
            for npc in self.patrol:
                if npc.is_dead() == False:
                    done = False
                    break

            if done == False:
                enemy = self.living_npc()
                c = random.choice(self.state.get_characters())
                if random.random() > 0.2 or (len(enemy.injuries) > 0 and random.random() > 0.5):
                    if c.challenge('combat'): # c attacks e
                        md_writer.print_chapter_sentence(self.hit_sentence(c, enemy))
                        enemy.add_injury(c)
                    else: # c misses e
                        md_writer.print_chapter_sentence(self.miss_sentence(c, enemy))
                else: # e attack c
                    if not c.challenge('combat'):
                        md_writer.print_chapter_sentence(self.hit_sentence(enemy, c))
                        c.add_injury(enemy)
                    else: # e misses c
                        md_writer.print_chapter_sentence(self.miss_sentence(enemy, c))

        md_writer.print_chapter_sentence("All of the " + pattern.en.pluralize(race) + " were defeated.")
