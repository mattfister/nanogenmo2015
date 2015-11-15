from paragraph import Paragraph
from wordtools import md_writer
import random
import pattern.en


class CampParagraph(Paragraph):

    def __init__(self, state):
        super(CampParagraph, self).__init__(state)

        self.method = random.choice(['hunting', 'searching for food', 'fishing'])

    def generate_sentences(self):
        md_writer.print_chapter_sentence(self.state.character_list() + " made camp.")

        energy = 0

        cs = self.state.get_characters()
        random.shuffle(cs)
        c1 = cs[0]
        c2 = cs[1]
        c3 = cs[2]

        sentences = []

        if random.random() < 0.05:
            md_writer.print_chapter_sentence(self.state.get_current_setting().mood_sentence())

        md_writer.print_chapter_sentence(c1.get_name() + ' searched for dry wood for a fire.')
        if c1.challenge('survival'):
            wood_found = random.choice(['dry ash kindling', ' birch twigs', 'large dried mushrooms', 'grassy dried reeds', 'dessicated cow dung'])
            location = random.choice(['in a nearby copse', 'inside a hollow log', 'beneath a spindly pine', 'along the ' + self.state.get_current_setting().get_name() + ' floor'])
            md_writer.print_chapter_sentence(c1.get_pronoun().title() + ' found ' + wood_found + ' ' + location + '.')
            fire_sound = random.choice(['roaring', 'crackling', 'hissing'])
            fire_type = random.choice(['campfire', 'blaze', 'bonfire'])
            md_writer.print_chapter_sentence(c2.get_name() + ' started a ' + fire_sound + ' ' + fire_type + '.')
            energy += 5
            md_writer.print_chapter_sentence('While ' + c1.get_name() + ' and ' + c2.get_name() + ' made a fire, ' + c3.get_name() + ' scouted around the campsite.')
        else:
            md_writer.print_chapter_sentence(c1.get_pronoun().title() + ' searched for an hour, but all the wood was wet, and ' + c1.get_pronoun() + ' gave up' + '.')
            md_writer.print_chapter_sentence('Meanwhile, ' + c3.get_name() + ' went scouting.')

        if random.random() < 0.05:
            md_writer.print_chapter_sentence(self.state.get_current_setting().mood_sentence())

        if c3.challenge('survival'):
            sense = random.choice(['saw', 'heard', 'spotted', 'noticed', 'observed'])
            grouping = random.choice(['band', 'family', 'patrol'])
            critter = random.choice(self.words.fantasy_races)
            critter = pattern.en.pluralize(critter)
            md_writer.print_chapter_sentence(c3.get_pronoun().title() + ' ' + sense + ' a ' + grouping + ' of ' + critter + '.')
            watching_adj = random.choice(['quietly', 'patiently', 'tirelessly'])
            md_writer.print_chapter_sentence(c3.get_pronoun().title() + ' ' + watching_adj + ' watched the ' + critter +'.')
            if (len(self.state.get_current_setting().get_known_props()) > 0):
                prop = random.choice(self.state.get_current_setting().get_known_props())
                md_writer.print_chapter_sentence('The ' + critter + ' took the ' + prop + ' from the ' + self.state.get_current_setting().get_name() + '.')
            md_writer.print_chapter_sentence('But the ' + critter + ' soon left the ' + self.state.get_current_setting().get_name() + '.')
            energy += 5
        else:
            critter = random.choice(self.words.fantasy_races)
            self.state.add_enemy_patrol(critter)
            critter_description = c3.get_pronoun().title() + " thought " + c3.get_pronoun() + ' saw ' + pattern.en.pluralize(critter) + ' in the distance.'
            md_writer.print_chapter_sentence(critter_description)
            failure = random.choice(['fell in a hidden gorge', 'loudly broke a branch', 'accidentally knocked over a boulder', 'fell asleep', 'walked into a tree'])
            md_writer.print_chapter_sentence(c3.get_pronoun().title() + ' suddenly ' + failure + '.')

        night_description = random.choice(['inky', 'black', 'moonlit', 'silent', 'calm'])
        md_writer.print_chapter_sentence(night_description.title() + ' darkness fell over the camp.')

        c = random.choice(self.state.get_characters())
        if random.random() < 0.5:
            md_writer.print_chapter_sentence(c.get_name() + ' told a story.')
        else:
            md_writer.print_chapter_sentence(c.get_name() + ' sang a song from ' + c.get_possessive_pronoun() + ' childhood.')

        sleep_opening = random.choice(['As the fire crackled', 'While the wind gusted', 'As gentle rain fell', 'As the leaves rustled', 'As howls were heard in the distance', 'As the moon shone overhead', 'Although sadness washed over them'])
        md_writer.print_chapter_sentence(sleep_opening + ',' + ' they all fell asleep.')

        c = random.choice(self.state.get_characters())
        md_writer.print_chapter_sentence(c.get_name() + ' dreamt of a ' + self.words.get_fantasy_place() + ', ' + self.words.get_fantasy_occupation() + ', and ' + self.words.get_living_thing_adj() + ' ' + pattern.en.pluralize(self.words.get_living_thing()) + '.')
        energy += 5

        self.state.add_energy(energy)