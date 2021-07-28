import sys
from .player_class import Player

sys.path.append("..")
from src import lenguages

class CPU(Player):

    def __init__(self):
        self.hand = []
        self.offhand = []
        self.score = 0
        self.flip_state = False
        self.name = f"CPU_{len(Player.player_list)}"

        Player.player_list.append(self)
    
    def __repr__(self):
        return self.name
    

    def play(self, table):
        def trail():
            print(str(self) + lenguages[Player.leng]["CPU_class"]["trail"] + self.hand[-1].display_name)
            table.top.append(self.hand.pop())
        
        def capture():
            for card_hand in self.hand:
                for card_top in table.top:
                    if card_hand == card_top:
                        print(str(self) + lenguages[Player.leng]["CPU_class"]["capture"][0] + card_top.display_name + lenguages[Player.leng]["CPU_class"]["capture"][1] + card_hand.display_name )
                        self.offhand.append(self.hand.pop(self.hand.index(card_hand)))
                        self.offhand.append(table.top.pop(table.top.index(card_top)))
                        return False
            return True
        if capture():
            trail()
        input(self.name + lenguages[Player.leng]["CPU_class"]["play"])
        

if __name__ == "__main__":
    pass
