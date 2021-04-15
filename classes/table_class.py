
class Table:
    def __init__(self, deck, player_list):
        self.top = []
        self.deck = deck
        self.player_list = player_list
        self.round = 1
    
    #Returns the top value
    def get_top(self):
        return self.top
    
    #Returns the round value
    def get_round(self):
        return self.round
    
    #Adds the parameter to the card
    def add_to_top(self,card):
        self.top.append(card)
        pass
    
    #Adds one round to the table
    def add_to_round(self):
        self.round += 1
        pass
    
    #Remove the target card from the top of the table
    def remove_from_top(self,target):
        return self.top.pop(self.top.index(target))
    
    #Used for displaying the cards at the top of the table.
    def display_top(self):
        cards_on_top = []
        index_helper = []
        for card in self.top:
            index_helper.append(str(len(cards_on_top)) + " ")
            cards_on_top.append(card.display_name)
        return print("Table \n", index_helper,"\n", cards_on_top, "\n")

    #Deal the cards to the players
    def deal(self):
        for _ in range(0,4):
            for player in self.player_list:
                player.add_to_hand(self.deck.remove_last_card())
    
    #Used for the start up of the batch
    def startup(self):
        for _ in range(0,4):
            self.add_to_top(self.deck.remove_last_card())
        self.deal()
        pass
    
    #Used for
    def next_round(self):
        self.add_to_round()
        self.deal()
        pass

if __name__ == "__main__":
    pass