from .deck_class import Deck

class Table:
    def __init__(self, player_list):
        self.top = []
        self.deck = ""
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
        if len(self.deck.container) == len(self.player_list) * 4:
            self.round = "Last Round"
        elif self.deck.container == []:
            self.round = "Stop"
        else:
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
            h = str(len(cards_on_top))
            i = len(card.display_name) - len(h)
            if i != 0:
                h = h + (" " * i)
            index_helper.append(h)
            cards_on_top.append(card.display_name)
        return print("Table \n", index_helper,"\n", cards_on_top, "\n")

    def display_round(self):
        return print("Round: " + str(self.round) + "\n")

    #Deal the cards to the players
    def deal(self):
        for _ in range(0,4):
            for player in self.player_list:
                player.add_to_hand(self.deck.remove_last_card())
    
    #Used for the start up of the batch
    def startup(self):
        self.deck = Deck()
        for _ in range(0,4):
            self.add_to_top(self.deck.remove_last_card())
        self.deal()
        pass
    
    #Used for passing to the next round
    def next_round(self):
        if self.round is not "Last round":
            self.add_to_round()
            if self.round is not "Stop":
                self.deal()



    #Used for passing to the next batch
    def next_batch(self):
        #Creates the dictionary
        players = {}

        #Creates the entry on the dictionary
        for player in self.player_list:
            players[player] = {
            "Cards": len(player.offhand),
            "Spades": 0
            }
        
        #Modifies the entry on the dictionary / Give the player score for the A's, 2♠ and 10♦
        for player in players:
            for card in player.offhand:
                if card.value == 1:
                    player.score += 1
                    print(f"{player}Scored a point. Reason:{card.display_name}")
                if card.symbol == "spade":
                    if card.value == 2:
                        player.score += 1
                        print(f"{player}Scored a point. Reason:{card.display_name}")
                    players[player]["Spades"] += 1
                if card.symbol == "diamond" and card.value == 10:
                    player.score += 2
                    print(f"{player}Scored two points. Reason:{card.display_name}")
        
        #Finishes the give the score to the player
        most_Cards = [0,""]
        most_Cards2 = 0

        most_Spades = [0,""]
        most_Spades2 = 0

        for player in players:
            if players[player]["Cards"] > most_Cards[0]:
                most_Cards[0], most_Cards[1] = players[player]["Cards"], player
            elif players[player]["Cards"] == most_Cards[0]:
                most_Cards2 = players[player]["Cards"]


            if players[player]["Spades"] > most_Spades[0]:
                most_Spades[0], most_Spades[1] = players[player]["Spades"], player
            elif players[player]["Spades"] == most_Spades[0]:
                most_Spades2 = players[player]["Spades"]

            #Clears the offhand of the player
            print(player.name, player.score)
            player.offhand.clear()

        if most_Cards[0] != most_Cards2:
            most_Cards[1].score += 3
            print(f"{player}Scored three points. Reason: Owns most cards")
        
        if most_Spades[0] != most_Spades2:
            most_Spades[1].score += 1
            print(f"{player}Scored a point. Reason: Owns most spades")
        #Clears the top
        self.top.clear()

        self.round = 1
        pass

if __name__ == "__main__":
    pass