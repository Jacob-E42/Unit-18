"""Word Finder: finds random words from a dictionary."""
from random import choice, randint


class WordFinder:
    """

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random() in wf.lines
    True

   
    """

    def __init__(self, path):
        self.path = path
        self.lines = self.readwords()
        print(f"{len(self.lines)} words read")
    def random(self):
   
        return choice(self.lines)

    def readwords(self):
        lines = []

        with open(self.path) as file:
            while (line := file.readline().rstrip()):
                lines.append(line)
            return lines

