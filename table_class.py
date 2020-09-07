
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
        
    def remove_from_top(self,target):
        return self.top.pop(self.top.index(target))

    def set_top(self,p):
        self.top = p
    
    
    def display_top(self):
        output = []
        for card in self.top:
            output.append(card.display_name)
        return output

    def deal(self, deck, player_list):
        for _ in range(0,4):
            for player in player_list:
                player.add_to_hand(deck.remove_last_card())
    
    def startup(self, deck, player_list):
        for _ in range(0,4):
            self.add_to_top(deck.remove_last_card())
        self.deal(deck, player_list)

if __name__ == "__main__":
    pass