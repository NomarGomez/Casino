
class Table:
    def __init__(self, deck):
        self.top = []
        self.deck = deck
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
    
    
    def display_top(self):
        output = []
        for card in self.top:
            output.append(card.display_name)
        return print("Table \n", output, "\n")

    def deal(self, player_list):
        for _ in range(0,4):
            for player in player_list:
                player.add_to_hand(self.deck.remove_last_card())
    
    def startup(self, player_list):
        for _ in range(0,4):
            self.add_to_top(self.deck.remove_last_card())
        self.deal(player_list)

if __name__ == "__main__":
    pass