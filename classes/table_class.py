
class Table:
    def __init__(self, deck, player_list):
        self.top = []
        self.deck = deck
        self.player_list = player_list
        self.round = 1
    

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
        cards_on_top = []
        index_helper = []
        for card in self.top:
            index_helper.append(str(len(cards_on_top)) + " ")
            cards_on_top.append(card.display_name)
        return print("Table \n", index_helper,"\n", cards_on_top, "\n")

    def deal(self):
        for _ in range(0,4):
            for player in self.player_list:
                player.add_to_hand(self.deck.remove_last_card())
    
    def startup(self):
        for _ in range(0,4):
            self.add_to_top(self.deck.remove_last_card())
        self.deal()
        pass
    
    def next_round(self):
        self.add_to_round()
        self.deal()
        pass

if __name__ == "__main__":
    pass