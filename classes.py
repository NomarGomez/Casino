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
    def add_to_offhand(self,card):
        self.offhand.append(card)
    def remove_from_hand(self,card):
        return self.hand.pop(card)
    def set_hand(self,p):
        self.hand = p
    

    def play(self,Input,instance):
        if isinstance(Input,int):
            card = self.remove_from_hand(Input)
        elif Input in self.hand:
            card = self.remove_from_hand(self.hand.index(Input))
        else:
            return print(f"{Input} isn't valid") 
        return card

class CPU(Player):
    def play(self):
        pass


class Table:
    def __init__(self):
        self.top = []
        self.round = 0
    

    def get_on_top(self):
        return self.top
    def get_round(self):
        return self.round
    
    def add_to_top(self,card):
        self.top.append(card)
    def add_to_round(self):
        self.round += 1
    def set_top(self,p):
        self.top = p