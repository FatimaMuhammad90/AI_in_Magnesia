from magnesia.laws.Laws import *

class PropertyClass:
    def  __init__(self, name, min_property, max_property):
        self.name = name
        self.min_property = min_property
        self.max_property = max_property


class Citizen:
    def __init__(self, name, age, property_class, occupation, personality):
        self.name = name
        self.age = age
        self.property_class = property_class
        self.occupation = occupation
        self.personality = personality

citizen1 = Citizen("Damon", 45, "Class I", "Landowner", "Conservative personality")

citizen2 = Citizen("Timon", 38, "Class II", "Farmer", "Practical personality" )

citizen3 = Citizen("Philon", 31, "Class II", "Craftsman", "Argumentative personality" )

citizen4 = Citizen("Herdotus", 27, "Class III", "Farmer", "Ambitious personality" )

citizen5 = Citizen("Marcus", 24, "Class IV", "Laborer", "Skeptical personality" )


