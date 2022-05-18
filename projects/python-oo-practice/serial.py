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

    def __init__(self, start=100):
        self.start = start
        self.serialNumber = start
    def generate(self):
        val = self.serialNumber
        self.serialNumber += 1
        return val

    def reset(self):
        self.serialNumber = self.start


