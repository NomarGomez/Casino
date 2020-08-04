from classes import Player, Table
from card_class import Card, values, symbols, deck_Of_Cards
table = Table()
mainPlayer = Player()
print(deck_Of_Cards)
card1 = Card(1,"spade")
mainPlayer.add_to_hand(card1.name)
print(mainPlayer.hand)
mycard = mainPlayer.play("A_spade", table)
print(mainPlayer.hand)
print(mycard)