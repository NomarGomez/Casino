from .player_class import Player


class CPU(Player):

    def __init__(self):
        super().__init__()
        self.name = f"CPU_{len(Player.player_list)}"
    
    def __repr__(self):
        return self.name
    

    def play(self, table):
        def trail():
            print(f"{self} will trail {self.hand[-1].display_name}")
            table.top.append(self.hand.pop())
        
        def capture():
            for card_hand in self.hand:
                for card_top in table.top:
                    if card_hand == card_top:
                        print(f"{self} will take {card_top.display_name} with {card_hand.display_name}")
                        self.offhand.append(self.hand.pop(self.hand.index(card_hand)))
                        self.offhand.append(table.top.pop(table.top.index(card_top)))
                        return False
            return True
        if capture():
            trail()
        input(f"{self.name} has ended his turn click enter to continue \n")
        

if __name__ == "__main__":
    pass
