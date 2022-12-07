"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __repr__(self):
        """ Show Representation """
        return f'<SerialGenerator start={self.start} current={self.current}>'

    def __init__(self, start):
        """
        Constructor that accepts one argument < start = int >
        There is also a current state that holds the current amount

        """
        self.start = self.current = start

    def generate(self):
        """
        Method that increments by 1 and returns the current total

        """
        self.current += 1
        return self.current - 1

    def reset(self):
        """
        Reset start to the original state that was given in the contructor
        """
        self.current = self.start
