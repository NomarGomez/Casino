
class Table:
    def __init__(self):
        self.top = []
        self.round = 0
    

    def get_top(self):
        return self.top
    
    def get_round(self):
        return self.round
    

    def add_to_top(self,card):
        self.top.append(card)
    
    def add_to_round(self):
        self.round += 1
    
    def set_top(self,p):
        self.top = p
    

    def display_top(self):
        p = []
        for card in self.top:
            p.append(card.display_name)
        return p

    def deal(self, deck, player_list):
        for _ in range(0,4):
            for player in player_list:
                player.add_to_hand(deck.remove_last_playing_card())
    
    def startup(self, deck, player_list):
        for _ in range(0,4):
            self.add_to_top(deck.remove_last_playing_card())
        self.deal(deck, player_list)
