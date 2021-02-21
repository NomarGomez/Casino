from build_class import Build
from card_class import Card


class Player:
    player_list = []

    def __init__(self):
        self.hand = []
        self.offhand = []
        self.owns = 0
        Player.player_list.append(self)
    
    def __repr__(self):
        return "Main Player "

    def add_to_owns(self, inter):
        self.owns += inter

    def get_hand(self):
        return self.hand
    
    def get_offhand(self):
        return self.offhand
    

    def add_to_hand(self,card):
        self.hand.append(card)
    
    def add_to_offhand(self,card):
        self.offhand.append(card)
    
    def remove_from_hand(self,card):
        return self.hand.pop(self.hand.index(card))
    
    def set_hand(self,cards):
        self.hand = cards

    
    def display_hand(self):
        output = []
        for card in self.hand:
            output.append(card.display_name)
        return print("Main-hand\n", output, "\n")
    
    def display_offhand(self):
        output = []
        for card in self.offhand:
            output.append(card.display_name)
        return print("Off-hand\n", output, "\n")
    
    def play(self,table):
        def input_to_key(Input, instance):
            try:
                key = int(Input)
                try:
                    instance[key]
                    return key
                except IndexError:
                    print(f"Unable to find the card. Reason: \"{Input}\" is out of range, please follow the instructions and try again ")
                    self.play(table)
            except ValueError:
                print(f"Unable to find the card, Reason: \"{Input}\" isn't a whole number, please follow the instructions and try again ")
                self.play(table)
            pass

        def find_target(key, instance):
            target = instance[key]
            return target

        #It have upper "H" because there is a built-in "help".
        def Help():
            print("How-to-play ")
            self.play(table)
            pass
        
        def drop():
            target = input("Select wich card do you want to drop ")
            card_hand = find_target(input_to_key(target, self.hand),self.hand)
            if self.owns == 0:
                no_other_card = True
                for obj in table.top:
                    if isinstance(obj,Card) and card_hand == obj:
                        no_other_card = False
                        break
                if no_other_card:
                    card = self.remove_from_hand(card_hand)
                    table.add_to_top(card)
                else:
                    print(f"Unable to drop \"{card_hand.display_name}\", Reason: \"{obj.display_name}\" it has the same value ")
                    self.play(table)
            else:
                print(f"Unable to drop \"{card_hand.display_name}\", Reason: You already own a build and you need to capture it build before trail or droping a card ")
                self.play(table)
            pass

        def capture():
            target_hand = input("Select wich card on your hand do you want to use ")
            targets_table = input("Select wich card, cards or build do you want to capture ")

            card_hand = find_target(input_to_key(target_hand, self.hand), self.hand)
            targets_table = targets_table.split()
            object_list = []
            targets_value = 0
            for index in range(len(targets_table)):
                target = input_to_key(targets_table[index], table.top)
                targets_table[index] = target
                obj = find_target(target, table.top)
                if isinstance(obj,Card):
                    targets_value += obj.value
                elif isinstance(obj,Build):
                    if card_hand != obj: 
                        pass
                object_list.append(obj)

            if len(targets_table) == len(set(targets_table)):
                if card_hand == targets_value:
                    self.add_to_offhand(self.remove_from_hand(card_hand))
                    for target in object_list:
                        self.add_to_offhand(table.remove_from_top(target))
                else:
                    print("The value of the card in your hand isn't equal to the value of the targets in the table, please follow instructions and try again ")
                    self.play(table)
            else:
                print("You selected two or more times the same object, please follow instructions and try again ")
                self.play(table)

            pass


        def build():
            pass
            
        commands = {
            "help" : Help,
            "drop" : drop,
            "trail": drop,
            "capture": capture,
            "build": build
        }

        action = input("Select an action ")

        try:
            commands[action]()
        except KeyError:
            print(f"\"{action}\" isn't a valid action, please type 'help' to see the actions available ")
            self.play(table)

class CPU(Player):

    def __init__(self):
        super().__init__()
        self.name = f"CPU_{len(Player.player_list)}"
    
    def __repr__(self):
        return f"CPU_{self.name}"
    

    def play(self, deck):
        pass

if __name__ == "__main__":
    pass
