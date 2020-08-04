
class Player:
    player_list = []
    def __init__(self):
        self.hand = []
        self.offhand = []
        Player.player_list.append(self)
    def __repr__(self):
        return "Main Player"

    def get_hand(self):
        return self.hand
    def get_offhand(self):
        return self.offhand
    
    def add_to_hand(self,card):
        self.hand.append(card)
    def add_to_offhand(self,card):
        self.offhand.append(card)
    def remove_from_hand(self,card):
        return self.hand.pop(card)
    def set_hand(self,p):
        self.hand = p

    
    def display_hand(self):
        p = []
        for card in self.hand:
            p.append(card.display_name)
        return p

    def play(self,Input,deck):
        if isinstance(Input,int):
            card = self.remove_from_hand(Input)
        elif Input in self.hand:
            card = self.remove_from_hand(self.hand.index(Input))
        else:
            return print(f"{Input} isn't a valid Input") 
        return card

class CPU(Player):
    def __init__(self, n):
        super().__init__()
        self.n = n
    def __repr__(self):
        return f"CPU_{self.n}"
    
    def play(self, deck):
        pass


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
        for i in range(0,4):
            for player in player_list:
                player.add_to_hand(deck.remove_last_playing_card())
    def startup(self, deck, player_list):
        for i in range(0,4):
            self.add_to_top(deck.remove_last_playing_card())
        self.deal(deck, player_list)