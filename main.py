#Loading modules

from classes import Player, Deck, Table


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