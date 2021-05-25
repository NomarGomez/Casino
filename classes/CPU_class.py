from .player_class import Player


class CPU(Player):

    def __init__(self):
        super().__init__()
        self.name = f"CPU_{len(Player.player_list)}"
    
    def __repr__(self):
        return f"CPU_{self.name}"
    

    def play(self, table):
        pass

if __name__ == "__main__":
    pass
