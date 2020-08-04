from classes import Player, CPU, Table
from card_class import Card, Deck

#Python 3x Python 3x


table = Table()

mainPlayer = Player()
cpu = CPU(1)

deck_Of_Cards = Deck()

print(deck_Of_Cards.display_container())
print("                                                                                                               ")

table.startup(deck_Of_Cards, Player.player_list)
print(deck_Of_Cards.display_container())
print("                                                                                                               ")

print(table.display_top())
print("                                                                                                               ")
print(mainPlayer.display_hand())
print(cpu.display_hand())