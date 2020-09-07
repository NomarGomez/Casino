from player_class import Player, CPU
from table_class import Table
from card_class import Card
from deck_class import Deck

#Build in Python 3.8.5

if __name__ == "__main__":
    table = Table()

    mainPlayer = Player()
    deck_Of_Cards = Deck()

    print("Deck")
    print (deck_Of_Cards.display_container())
    print("                                                    ")
    table.startup(deck_Of_Cards, Player.player_list)

    print("Table")
    print(table.display_top())
    print("Main player hand")
    print (mainPlayer.display_hand())
    mainPlayer.play(table)
    print("                                                    ")

    #mainPlayer.play(table)
    print("                                                    ")
    print("Table")
    print(table.display_top())
    print("Main player hand")
    print(mainPlayer.display_hand())
    print("Main player offhand")
    print(mainPlayer.display_offhand())