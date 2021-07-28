#Loading modules

from classes import Player, CPU, Table, Menu

from functions import clearDisplay

Menu()

#Build in Python 3.9x
if __name__ == "__main__":
    table = Table(Player.player_list)
    lastest_player = "" #Lastest player that play
    #Loop of a game
    while table.game_state:
        #Loop of a batch
        table.startup()
        while table.round != "Stop":
            #Loop of a round (A player must play 4 times)
            for _ in range(0,4):
                #Players play one at time
                for player in table.player_list:
                    if isinstance(player,Player):
                        lastest_player = player
                    clearDisplay()
                    table.display_scoreboard()
                    table.display_round()
                    table.display_top()
                    lastest_player.display()

                    player.play(table)
            table.next_round()        
        table.next_batch()
    table.game_over()