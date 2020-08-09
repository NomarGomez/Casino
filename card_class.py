import random


class Card:
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

    def __init__(self, value, symbol):
        self.value = value
        self.symbol = symbol
        self.name = f"{Card.values[value]}_{symbol}"
        self.display_name = f"{Card.values[value]}{Card.symbols[symbol]}"
    
    def __repr__(self):
        return f"{self.name}"


class Deck:
    figures = ["spade", "clover", "heart", "diamond"]
    def __init__(self):
        self.playing_cards = []
        for symb in Deck.figures:
            for val in range(1, 14):
                self.playing_cards.append(Card(val,symb))
        random.shuffle(self.playing_cards)
    

    def get_playing_cards(self):
        return self.playing_cards


    def remove_last_playing_card(self):
        return self.playing_cards.pop()


    def display_playing_cards(self):
        p = []
        for card in self.playing_cards:
            p.append(card.display_name)
        return p
