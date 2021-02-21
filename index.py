from player_class import Player, CPU
from table_class import Table
from card_class import Card
from deck_class import Deck

#Build in Python 3.8.5

if __name__ == "__main__":
    mainPlayer = Player()
    deck_Of_Cards = Deck()

    table = Table(deck_Of_Cards)


    deck_Of_Cards.display_container()

    table.startup(Player.player_list)
    while True:
        table.display_top()
        mainPlayer.display_hand()
        mainPlayer.play(table)

        mainPlayer.display_offhand()
        
        if len(mainPlayer.get_hand()) == 0:
            table.deal(Player.player_list)