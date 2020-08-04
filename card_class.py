import random
symbols = {
    "spade": "♠",
    "clover": "♣",
    "heart": "♥",
    "diamond": "♦"
}

values = {
    1: "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K"
}
figures = ["spade", "clover", "heart", "diamond"]
deck_Of_Cards = []
class Card:
    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol
        self.name = f"{values[value]}_{symbol}"
        self.display_name = f"{values[value]}{symbols[symbol]}"
for symb in figures:
    for val in range(1, 14):
        deck_Of_Cards.append(Card(val,symb).name)
random.shuffle(deck_Of_Cards)