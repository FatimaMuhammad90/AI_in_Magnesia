from magnesia.laws.Laws import LAWS
class Magnesia:
    def __init__(self):
        self.citizens = []
        self.laws = LAWS
        self.year = 1

    def add_citizen(self, citizen):
        self.citizens.append(citizen)