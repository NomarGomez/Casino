#Loading modules

from classes import Player, Deck, Table


#Build in Python 3.8.5

if __name__ == "__main__":
    mainPlayer = Player()
    deck_Of_Cards = Deck()

    table = Table(deck_Of_Cards, Player.player_list)
    #Loop of a game
    while True:
        #Loop of a batch
        table.startup()
        while True:
            #Loop of a round (A player must play 4 times)
            for _ in range(0,4):
                #Players play 1 time
                for player in table.player_list:
                    table.display_top()
                    mainPlayer.display_hand()
                    mainPlayer.display_offhand()

                    player.play(table)

            table.next_round()