"""Word Finder: finds random words from a dictionary, excluding comments and blank lines."""
from wordfinder import WordFinder
class SpecialWordFinder(WordFinder):
    """

    >>> wf = SpecialWordFinder("words.txt")
    235886 words read

    >>> wf.random() in wf.lines
    True

   
    """
    def __init__(self, path):
        super().__init__(path)
    def readwords(self):

        with open(self.path) as file:
            lines =  [line.rstrip() for line in file.readlines() if line[0] != "#" and line[0].isspace() is not True]
            
            return lines
