from wordfinder import WordFinder


class SpecialWordFinder(WordFinder):
    """ 
    Machine that removes comments # and empty lines in file path
    >>> swf = SpecialWordFinder('specialwords.txt')
    4 words read
    >>> from random import seed
    >>> seed(4)
    >>> swf.random()
    'parsnips'
    >>> swf.random() in swf.parsed_data
    True
    """

    def __init__(self, file):
        """inherits from WordFinder class"""
        super().__init__(file)

    def __repr__(self):
        """Show Representation"""
        return f"<SpeciaWrodFinder file='{self.file}'>"

    def parse_file(self):
        """ Parses file path that removes comments and blank lines """
        with open(self.file, mode='r', encoding='utf-8') as f:
            read_line = []
            for line in f.readlines():
                if '#' not in line and len(line) > 1:
                    read_line.append(line.strip())
            return read_line
