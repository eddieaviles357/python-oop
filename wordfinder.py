"""Word Finder: finds random words from a dictionary."""
from random import randint, choice


class WordFinder:
    """
    Machine to finding words in test files
    >>> wf = WordFinder("words.txt")
    235886 words read
    >>> from random import seed
    >>> seed(235885)
    >>> wf.random()
    'pleomorph'
    >>> wf.random() in wf.parsed_data
    True
    """

    def __init__(self, file):
        """
        Constructor that accepts a file.txt path and prints out the
        total lines read
        """
        self.file = file
        self.parsed_data = self.parse_file()
        print(f"{len(self.parsed_data)} words read")

    def __repr__(self):
        """Show Representation"""
        return f"<WordFinder file='{self.file}'>"

    def parse_file(self):
        """ Reads and returns a list with no new line char \n """
        with open(self.file, mode='r', encoding='utf-8') as f:
            read_lines = []
            for line in f.readlines():
                read_lines.append(line.strip())
            return read_lines

    def print_file(self):
        """ return a list of all the data parsed when initialized """
        return self.parsed_data

    def random(self):
        """ returns a random word in parsed_data """
        return choice(self.parsed_data)
