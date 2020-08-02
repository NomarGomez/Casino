from card import newDeck

class Player:
    def __init__(self):
        self.hand = []
        self.offhand = []

    def get_hand(self):
        return self.hand
    def get_offhand(self):
        return self.offhand
    
    def add_to_hand(self,card):
        self.hand.append(card)

mainPlayer = Player()