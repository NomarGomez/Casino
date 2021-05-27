from .player_class import Player


class CPU(Player):

    def __init__(self):
        super().__init__()
        self.name = f"CPU_{len(Player.player_list)}"
    
    def __repr__(self):
        return f"CPU_{self.name}"
    

    def play(self, table):
        def trail():
            table.top.append(self.hand.pop())
        
        def capture():
            for card_hand in self.hand:
                for card_top in table.top:
                    if card_hand == card_top:
                        self.offhand.append(self.hand.pop(self.hand.index(card_hand)))
                        self.offhand.append(table.top.pop(table.top.index(card_top)))
                        return False
            return True
        if capture():
            trail()
        

if __name__ == "__main__":
    pass
