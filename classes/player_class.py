
class Player:
    player_list = []

    def __init__(self):
        self.hand = []
        self.offhand = []
        self.name = ""
        self.score = 0

        Player.player_list.append(self)
    
    #Changes how is represented (printed) the Player Object
    def __repr__(self):
        return "Main Player "

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
            index_helper.append(str(len(cards_on_hand)) + " ")
            cards_on_hand.append(card.display_name)
        return print("Hand \n", index_helper,"\n", cards_on_hand, "\n")
    
    #Displays the offhand of the player
    def display_offhand(self):
        output = []
        for card in self.offhand:
            output.append(card.display_name)
        return print("\nOff-hand\n", output, "\n")
    
    def play(self,table):

        
        def input_to_key(Input, instance):
            try:
                key = int(Input)
                try:
                    instance[key]
                    return key
                except IndexError:
                    print(f"Unable to find the card. Reason: \"{Input}\" is out of range, please follow the instructions and try again ")
                    return self.play(table)
            except ValueError:
                print(f"Unable to find the card, Reason: \"{Input}\" isn't a whole number, please follow the instructions and try again ")
                return self.play(table)

        def find_target(key, instance):
            target = instance[key]
            return target

        #It have upper "H" because there is a built-in "help".
        def Help():
            print("How-to-play ")
            return self.play(table)
        
        def drop():
            target = input("Select wich card do you want to drop \n")
            card_hand = find_target(input_to_key(target, self.hand),self.hand)
            for card_top in table.top:
                if card_hand == card_top:
                    print(f"Unable to drop \"{card_hand.display_name}\", Reason: \"{card_top.display_name}\" have the same value ")
                    return self.play(table)
            table.add_to_top(self.remove_from_hand(card_hand))
            pass

        def capture():
            target_hand = input("Select wich card on your hand do you want to use \n")
            targets_table = input("Select wich card, cards or build do you want to capture \n")

            #Makes sure that the player didn't set two times the same card
            if len(targets_table) == len(set(targets_table)):

                card_hand = find_target(input_to_key(target_hand, self.hand), self.hand)
                targets_table = targets_table.split()
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
                    print("The value of the card in your hand isn't equal to the value of the targets in the table, please follow instructions and try again ")
                    return self.play(table)
            else:
                print("You selected two or more times the same card, please follow instructions and try again ")
                return self.play(table)
            pass

        commands = {
            "help" : Help,
            "drop" : drop,
            "trail": drop,
            "capture": capture,
        }

        action = (input("Select an action (help, drop, trail or capture):  \n")).lower()

        try:
            commands[action]()
        except KeyError:
            print(f"\"{action}\" isn't a valid action, please type 'help' to see the actions available ")
            return self.play(table)

if __name__ == "__main__":
    pass