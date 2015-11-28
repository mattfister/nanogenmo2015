from paragraph import Paragraph
from wordtools import md_writer
import random
import pattern.en
from says_sentence import says_sentence

class FoodParagraph(Paragraph):

    def __init__(self, state):
        super(FoodParagraph, self).__init__(state)

        self.method = random.choice(['hunting', 'searching for food', 'fishing'])

    def hunting(self, c):
        animal = random.choice(['rabbit', 'turkey', 'deer', 'boar', 'elk', 'caribou', 'sheep', 'bison', 'hare', 'raccoon', 'squirrel'])

        md_writer.print_chapter_sentence(c.get_pronoun().title() + ' searched the ' + self.state.get_current_setting().get_name() + ' for signs of ' + pattern.en.pluralize(animal) +".")

        # Find a place to hunt
        if c.challenge('survival'):
            md_writer.print_chapter_sentence(animal.title() + ' tracks were spotted by ' + c.get_possessive_pronoun() + ' in the mud.')
        else:
            md_writer.print_chapter_sentence('But ' + c.get_pronoun() + ' failed to find any ' + animal + ' signs.')
            return 0

        if random.random() < 0.05:
            md_writer.print_chapter_sentence(self.state.get_current_setting().mood_sentence())

        if c.challenge('survival'):
            md_writer.print_chapter_sentence(c.get_name() + ' followed the tracks, staying upwind so as not to alert the ' + animal + '.')
        else:
            md_writer.print_chapter_sentence(c.get_name() + ' followed the tracks, but the ' + animal + ' noticed ' + c.get_possessive_pronoun() + ' and ran.')
            return 0

        if random.random() < 0.05:
            md_writer.print_chapter_sentence(self.state.get_current_setting().mood_sentence())

        md_writer.print_chapter_sentence(c.get_pronoun().title() + ' aimed ' + c.get_possessive_pronoun() + ' bow at the ' + animal + ' and fired.')
        if c.challenge('survival'):
            md_writer.print_chapter_sentence(c.get_pronoun().title() + ' hit ' + c.get_possessive_pronoun() + ' target.')
        else:
            md_writer.print_chapter_sentence(c.get_pronoun().title() + ' fired, but missed.')
            md_writer.print_chapter_sentence('The ' + animal + ' ran off.')
            return 0

        return random.randint(7, 15)

    def searching(self, c):
        # Find a place to search for food
        food = random.choice(['bird eggs', 'wild barley', 'berries', 'mushrooms', 'almonds', 'chickpeas', 'wild carrots', 'olives', 'apples', 'bananas', 'avocados'])
        md_writer.print_chapter_sentence(c.get_name() + ' went searching for ' + food + '.')
        if c.challenge('survival'):
            md_writer.print_chapter_sentence(c.get_pronoun().title() + ' looked around the ' + self.state.get_current_setting().get_name() + ' for ' + food + '.')
        else:
            md_writer.print_chapter_sentence('After a lengthy search, ' + c.get_pronoun() + ' gave up - no ' + food + ' were to be found here.')
            return 0

        if random.random() < 0.05:
            md_writer.print_chapter_sentence(self.state.get_current_setting().mood_sentence())

        # Gather the food
        if c.challenge('survival'):
            md_writer.print_chapter_sentence(c.get_name() + ' filled ' + c.get_possessive_pronoun() + ' arms with ' + food + '.')
        else:
            md_writer.print_chapter_sentence(c.get_name() + ' tasted the ' + food + '.')
            taste = random.choice(['bitter', 'disgusting', 'sour', 'dizzying', 'gross', 'fiery'])
            md_writer.print_chapter_sentence('It was ' + taste + '.')
            md_writer.print_chapter_sentence(says_sentence(c, 'Must be poisonous'))
            return 0

        return random.randint(7, 15)

    def fishing(self, c):
        fishing_location = random.choice(['clear pool', 'gentle stream', 'burbling brook', 'rapid river'])

        # Find a place to fish
        md_writer.print_chapter_sentence(c.get_pronoun().title() + ' searched the ' + self.state.get_current_setting().get_name() + ' for a place to go fishing.')
        if c.challenge('survival'):
            md_writer.print_chapter_sentence('Nearby, ' + c.get_pronoun() + ' found a ' + fishing_location + '.')
        else:
            md_writer.print_chapter_sentence(c.get_pronoun().title() + ' searched far and wide, but there were no suitable fishing locations nearby.')
            return 0

        if random.random() < 0.05:
            md_writer.print_chapter_sentence(self.state.get_current_setting().mood_sentence())

        # See what you catch
        md_writer.print_chapter_sentence(c.get_name() + " cast " + c.get_possessive_pronoun() + " net into the " + fishing_location + ".")

        fish_adj = random.choice(['', '', '', '', 'huge', 'slimey', 'gigantic', 'mutated', 'unusual', 'wiggly', 'smelly', 'odd', 'beautiful'])
        fish = fish_adj + ' ' + random.choice(['bass', 'catfish', 'trout', 'mud sunfish', 'bluegill', 'brown bullhead', 'black crappie', 'brown trout', 'carp', 'calico bass', 'channel catfish', 'creek chubsucker', 'chain pickerel', 'fallfish', 'green sunfish', 'largemouth bass', 'longnose sucker', 'pumpkinseed', 'rainbow trout', 'smallmouth bass', 'white catfish', 'white perch', 'white sucker', 'yellow bullhead', 'yellow perch'])
        if c.challenge('survival'):
            md_writer.print_chapter_sentence('There was a ' + random.choice(['sharp', 'gentle']) + ' tug on ' + c.get_possessive_pronoun() + ' line.')
            md_writer.print_chapter_sentence(c.get_name() + ' pulled in a ' + fish + '!')
            return random.randint(7, 10)
        else:
            md_writer.print_chapter_sentence('After a relaxing hour without any bites ' + c.get_name() + ' fell asleep and gave up on fishing.')
            return 0

    def generate_sentences(self):
        c1 = random.choice(self.state.get_characters())
        c = random.choice(self.state.get_characters())
        others = [char for char in self.state.get_characters() if char.get_name() != c.get_name()]
        md_writer.print_chapter_sentence(self.state.generate_food_sentence(c1))
        md_writer.print_chapter_sentence(c.get_name() + ' decided to go ' + self.method + '.')
        memory = c.get_memory(self.method)
        if memory != None:
            md_writer.print_chapter_sentence(memory)

        food = 0
        if self.method == 'hunting':
            food = self.hunting(c)
        elif self.method == 'searching for food':
            food = self.searching(c)
        else:
            food = self.fishing(c)

        if food > 0:
            md_writer.print_chapter_sentence(c.get_name() + ' returned to ' + others[0].get_name() + ' with ' + c.get_possessive_pronoun() + ' food.')
            md_writer.print_chapter_sentence(says_sentence(others[0], 'Great job ' + c.get_name()))
            c.set_positive_quality()
        else:
            md_writer.print_chapter_sentence(c.get_name() + ' returned to ' + others[0].get_name() + ' empty handed.')
            md_writer.print_chapter_sentence(says_sentence(c, "We will have to just keep going, there was no food to find here"))
            if random.random() < 0.5:
                c.set_negative_quality()

        self.state.add_food(food)

