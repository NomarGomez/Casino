
class Card:
    symbols = {
        "spade": "♠",
        "clover": "♣",
        "heart": "♥",
        "diamond": "♦"  
    }

    values_to_ranks = {
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
        self.name = f"{Card.values_to_ranks[value]}_{symbol}"
        self.display_name = f"{Card.values_to_ranks[value]}{Card.symbols[symbol]}"
    
    def __repr__(self):
        return f"{self.name}"
    def __eq__(self, other):
        value1, value2 = self.__eval(other)
        if value1 == value2:
            return True
        else:
            return False
            
    def __ne__(self, other): 
        value1, value2 = self.__eval(other)
        if value1 != value2:
            return True
        else:
            return False

    def __eval(self, other):
        if isinstance(other,Card):
            value1, value2 = self.value, other.value
            if value1 == 1:
                value1 = 14
            if value2 == 1:
                value2 = 14
            return value1, value2
        else:
            value1, value2 = self.value, other
            if value1 == 1:
                value1 = 14
            return value1, value2

if __name__ == "__main__":
    pass