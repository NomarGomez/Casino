import sys
import random

from .deck_class import Deck

sys.path.append("..")
from src import lenguages
from functions import clearDisplay


class Table:
    leng = ""
    def __init__(self, player_list):
        self.top = []
        self.deck = ""
        self.player_list = player_list
        self.round = 1
        self.scoreboard = lenguages[Table.leng]["table_class"]["blankscoreboard"]
        self.game_state = True
        self.winner = ""
    
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

    #Updates the scores
    def update_scoreboard(self):
        self.scoreboard = {}
        winners = []
        for player in self.player_list:
            if player.score >= 21:
                if winners == []:
                    winners.append(player)
                elif player.score > winners[0].score:
                    winners.clear()
                    winners.append(player)
                elif player.score == winners[0].score:
                    winners.append(player)

            self.scoreboard[player] = player.score
        if len(winners) == 1:
            self.winner = winners[0]
            self.game_state = False #This player won the game
        pass

    
    #Used for displaying the cards at the top of the table.
    def display_top(self):
        cards_on_top = []
        index_helper = []
        for card in self.top:
            #This is used to give blank spaces to the index helper so the two lists has the same lenght and looks prettier on the terminal
            h = str(len(cards_on_top))
            i = len(card.display_name) - len(h)
            if i != 0:
                h = h + (" " * i)
            index_helper.append(h)
            cards_on_top.append(card.display_name)
        return print(lenguages[Table.leng]["table_class"]["table"] + str(index_helper) + "\n" + str(cards_on_top) + "\n")

    #Display the current round
    def display_round(self):
        return print(lenguages[Table.leng]["table_class"]["round"] + str(self.round) + "\n")

    #Displays the scoreboard
    def display_scoreboard(self):
        return print(lenguages[Table.leng]["table_class"]["scoreboard"] + str(self.scoreboard) +  "\n")

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
            self.add_to_round()
            if self.round != "Stop":
                self.deal()



    #Used for passing to the next batch
    def next_batch(self):
        #Creates the dictionary
        players = {}

        input(lenguages[Table.leng]["table_class"]["nextbatch"][0])
        print(lenguages[Table.leng]["table_class"]["nextbatch"][1])
        clearDisplay()

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
                    print(str(player) + lenguages[Table.leng]["table_class"]["score"][0] + card.display_name)
                if card.symbol == "spade":
                    if card.value == 2:
                        player.score += 1
                        print(str(player) + lenguages[Table.leng]["table_class"]["score"][0] + card.display_name)
                    players[player]["Spades"] += 1
                if card.symbol == "diamond" and card.value == 10:
                    player.score += 2
                    print(str(player) + lenguages[Table.leng]["table_class"]["score"][1] + card.display_name)
        
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
            player.offhand.clear()

        if most_Cards[0] != most_Cards2:
            most_Cards[1].score += 3
            print(str(player) + lenguages[Table.leng]["table_class"]["score"][2])
        else:
            print(lenguages[Table.leng]["table_class"]["score"][3])
        
        if most_Spades[0] != most_Spades2:
            most_Spades[1].score += 1
            print(str(player) + lenguages[Table.leng]["table_class"]["score"][4])
        else:
            print(lenguages[Table.leng]["table_class"]["score"][5])

        input(lenguages[Table.leng]["table_class"]["score"][6])
        #Clears the table
        self.top.clear()
        self.round = 1

        #Shuffles the list of players so players play in differents turns
        random.shuffle(self.player_list)

        #Updates the scoreboard
        self.update_scoreboard()

        pass
    def game_over(self):
        clearDisplay()
        input(lenguages[Table.leng]["table_class"]["gameover"][0])

        print(lenguages[Table.leng]["table_class"]["gameover"][1] + self.winner)
        print(lenguages[Table.leng]["table_class"]["gameover"][2] + self.scoreboard)
        print(lenguages[Table.leng]["table_class"]["gameover"][3])

if __name__ == "__main__":
    pass