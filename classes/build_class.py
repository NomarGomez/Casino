class Build(list):
    def __init__(self, value, owner, card_attached):
        self.contains = []
        self.display_name = []
        self.value = value
        self.owner = owner
        self.card_attached = card_attached

        self.owner.add_to_owns(1)
    def __repr__(self):
        return repr(self.contains)


    def add_to_contains(self, set_of_cards):
        self.contains.append(set_of_cards)
        for card in self.contains:
            self.display_name.append(card.display_name)

    def retrieve(self):
        self.owner.add_to_owns(-1)
        del self
        pass

if __name__ == "__main__":
    pass