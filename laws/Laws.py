LAWS = {
    "four_property_classes": {
        "description": "Citizens are divided into four property classes.",
        "type": "social_structure"
    },

    "no_merchants": {
        "description": "Magnesian citizens cannot engage in merchant activity.",
        "type": "economic"
    },

    "city_away_from_sea": {
        "description": "The city is deliberately established away from the sea.",
        "type": "geography"
    }
}

class Law:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type

