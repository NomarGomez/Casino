import sys

#Relative import
sys.path.append("..")
from src.lenguages import lenguages

class Player:
    player_list = []
    gamemode = ""
    leng = ""
    def __init__(self,name):
        self.hand = []
        self.offhand = []
        self.name = name
        self.score = 0
        self.flip_state = True

        Player.player_list.append(self)
    
    #Changes how is represented (printed) the Player Object
    def __repr__(self):
        return self.name

    #Returns the hand of the player as an object
    def get_hand(self):
        return self.hand
    
    #Returns the offhand of the player as an object
    def get_offhand(self):
        return self.offhand
    
    #Adds a card to the player hand
    def add_to_hand(self,card):
        self.hand.append(card)
    
    #Adds a card to the player offhand
    def add_to_offhand(self,card):
        self.offhand.append(card)
    
    #Remvove a card from the player hands
    def remove_from_hand(self,card):
        return self.hand.pop(self.hand.index(card))
    
    #Set an specific hand of the player (For testing porpuses only)
    def set_hand(self,cards):
        self.hand = cards

    #Displays the hand of the player
    def display_hand(self):
        cards_on_hand = []
        index_helper = []
        for card in self.hand:
            h = str(len(cards_on_hand))
            i = len(card.display_name) - len(h)
            if i != 0:
                h = h + (" " * i)
            index_helper.append(h)
            cards_on_hand.append(card.display_name)
        return print(lenguages[Player.leng]["player_class"]["displayhand"] + str(index_helper) + "\n" + str(cards_on_hand) + "\n")
    
    def display_handflipped(self):
        cards_on_hand = []
        for card in self.hand:
            cards_on_hand.append("🂠")
        return print(lenguages[Player.leng]["player_class"]["displayhand"] + str(cards_on_hand))
    
    #Displays the offhand of the player
    def display_offhand(self):
        output = []
        for card in self.offhand:
            output.append(card.display_name)
        return print(lenguages[Player.leng]["player_class"]["displayoffhand"] + str(output) + "\n")
    
    def display(self):
        if Player.gamemode == "Singleplayer":
            self.display_hand()
            print(lenguages[Player.leng]["player_class"]["display"] + str(len(self.offhand)) + "\n")
            return
        else:
            if self.flip_state:
                self.display_handflipped()
                print( "\n" + lenguages[Player.leng]["player_class"]["display"] + str(len(self.offhand)) + "\n")
                return
            else:
                self.display_hand()
                print( "\n" + lenguages[Player.leng]["player_class"]["display"] + str(len(self.offhand)) + "\n")
                return
        pass

    def play(self,table):

        def flip():
            if self.flip_state:
                self.flip_state = False
                self.display()
            else:
                self.flip_state = True
            return self.play(table)

        def input_to_key(Input, instance):
            try:
                key = int(Input)
                try:
                    instance[key]
                    return key
                except IndexError:
                    print(lenguages[Player.leng]["player_class"]["inputokeye"] +  f" \"{Input}\" " + lenguages[Player.leng]["player_class"]["inputtokeye1"])
                    return self.play(table)
            except ValueError:
                print(lenguages[Player.leng]["player_class"]["inputokeye"] +  f" \"{Input}\" " + lenguages[Player.leng]["player_class"]["inputtokeye2"])
                return self.play(table)

        def find_target(key, instance):
            try:
                target = instance[key]
                return target
            except:
                return self.play(table)

        #It have upper "H" because there is a built-in "help".
        def Help():
            print(lenguages[Player.leng]["player_class"]["help"])
            return self.play(table)
        
        def drop():
            target = input(lenguages[Player.leng]["player_class"]["dropinput"])
            card_hand = find_target(input_to_key(target, self.hand),self.hand)
            for card_top in table.top:
                if card_hand == card_top:
                    print(lenguages[Player.leng]["player_class"]["droperror"][0] + f" \"{card_hand.display_name} ({self.hand.index(card_hand)})\" " + lenguages[Player.leng]["player_class"]["droperror"][1] + f" \"{card_top.display_name} ({table.top.index(card_top)}) \"" + lenguages[Player.leng]["player_class"]["droperror"][2])
                    return self.play(table)
            table.add_to_top(self.remove_from_hand(card_hand))
            pass

        def capture():
            target_hand = input(lenguages[Player.leng]["player_class"]["captureinput1"])
            targets_table = input().split(lenguages[Player.leng]["player_class"]["captureinput2"])

            #Makes sure that the player didn't set two times the same card
            if len(targets_table) == len(set(targets_table)):

                card_hand = find_target(input_to_key(target_hand, self.hand), self.hand)
                cards_list = []
                targets_value = 0
                for index in range(len(targets_table)):
                    target = input_to_key(targets_table[index], table.top)
                    targets_table[index] = target
                    card = find_target(target, table.top)
                    targets_value += card.value
                    cards_list.append(card)

                if card_hand == targets_value:
                    self.add_to_offhand(self.remove_from_hand(card_hand))
                    for target in cards_list:
                        self.add_to_offhand(table.remove_from_top(target))
                else:
                    print(lenguages[Player.leng]["player_class"]["captureerror1"])
                    return self.play(table)
            else:
                print(lenguages[Player.leng]["player_class"]["captureerror2"])
                return self.play(table)
            pass

        if Player.gamemode == "Singleplayer":
            commands = {
            lenguages[Player.leng]["player_class"]["commands"][0] : Help,
            lenguages[Player.leng]["player_class"]["commands"][1] : drop,
            lenguages[Player.leng]["player_class"]["commands"][2]: drop,
            lenguages[Player.leng]["player_class"]["commands"][3]: capture,
            }
        else:
            commands = {
            lenguages[Player.leng]["player_class"]["commands"][0] : Help,
            lenguages[Player.leng]["player_class"]["commands"][1] : drop,
            lenguages[Player.leng]["player_class"]["commands"][2]: drop,
            lenguages[Player.leng]["player_class"]["commands"][3]: capture,
            lenguages[Player.leng]["player_class"]["commands"][4]: flip,
            }
        
        action = input(self.name + lenguages[Player.leng]["player_class"]["action"]).lower()
        try:
            commands[action]()
        except KeyError:
            print(action  + lenguages[Player.leng]["player_class"]["actionerror"])
            return self.play(table)
        self.flip_state = True

if __name__ == "__main__":
    pass