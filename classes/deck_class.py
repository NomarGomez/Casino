import random

from .card_class import Card

class Deck:
    figures = ["spade", "clover", "heart", "diamond"]
    def __init__(self):
        self.container = []
        for symb in Deck.figures:
            for val in range(1, 14):
                self.container.append(Card(val,symb))
        random.shuffle(self.container)
    

    def get_container(self):
        return self.container


    def remove_last_card(self):
        return self.container.pop()


    def display_container(self):
        output = []
        for card in self.container:
            output.append(card.display_name)
        return print("Deck\n", output, "\n")

if __name__ == "__main__":
    pass
