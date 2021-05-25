#Loading modules

from classes import Player, Deck, Table


#Build in Python 3.9.2

if __name__ == "__main__":
    mainPlayer = Player()

    table = Table(Player.player_list)
    #Loop of a game
    while True:
        #Loop of a batch
        table.startup()
        while table.round != "Stop":
            #Loop of a round (A player must play 4 times)
            for _ in range(0,4):
                #Players play one at time
                for player in table.player_list:
                    table.display_round()
                    table.display_top()
                    mainPlayer.display_hand()
                    mainPlayer.display_offhand()

                    player.play(table)
            table.next_round()
        
        table.next_batch()