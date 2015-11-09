from wordtools import wordLists

class Paragraph(object):

    def __init__(self, state):
        self.state = state
        self.words = wordLists.WordLists()
