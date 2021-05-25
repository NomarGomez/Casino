from .deck_class import Deck

class Table:
    def __init__(self, player_list):
        self.top = []
        self.deck = ""
        self.player_list = player_list
        self.round = 0
    
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
        if self.deck != []:
            self.round += 1
        elif self.deck == []:
            self.round = "Last round"
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

    def display_round(self):
        return print("Round \n", self.round ,"\n")

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
        if self.round != "Last round":
            self.deal()
            self.add_to_round()
        else:
            self.round = "Stop"



    #Used for passing to the next batch
    def next_batch(self):
        #Creates the dictionary
        players = {}

        #Creates the entry on the dictionary
        for player in self.player_list:
            players[player.name] = {
            "Obj": player,
            "Cards": len(player.offhand),
            "Spades": 0
            }
        
        #Modifies the entry on the dictionary / Give the player score for the A's, 2♠ and 10♦
        for player in players:
            for card in player["Obj"].offhand:
                if card.value == 1:
                    player["Obj"].score += 1
                if card.symbol == "spade":
                    if card.value == 2:
                        player["Obj"].score += 1
                    player["Spades"] += 1
                if card.symbol == "diamond" and card.value == 10:
                    player["Obj"].score += 2
        
        #Finishes the give the score to the player
        most_Cards = [0,""]
        most_Cards2 = 0

        most_Spades = [0,""]
        most_Spades2 = 0

        for player in players:
            if player["Cards"] > most_Cards[0]:
                most_Cards[0], most_Cards[1] = player["Cards"], player["Obj"]
            elif player["Cards"] == most_Cards[0]:
                most_Cards2 = player["Cards"]


            if player["Spades"] > most_Spades[0]:
                most_Spades[0], most_Spades[1] = player["Spades"], player["Obj"]
            elif player["Spades"] == most_Spades[0]:
                most_Spades2 = player["Spades"]

            #Clears the offhand of the player
            player["Obj"].offhand.clear()
            pass

        if most_Cards[0] != most_Cards2:
            most_Cards[1].score += 3
        
        if most_Spades[0] != most_Spades2:
            most_Spades[1].score += 1

        #Clears the top
        self.top.clear()

        self.round = 0
        pass

if __name__ == "__main__":
    pass