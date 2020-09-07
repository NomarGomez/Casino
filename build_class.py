class Build(list):
    def __init__(self, value):
        self.contains = []
        self.value = value
        
    def __repr__(self):
        return self.contains


    def add_to_contains(self, set_of_cards):
        self.contains.append(set_of_cards)

    def retrieve(self):
        pass