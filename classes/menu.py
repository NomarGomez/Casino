import sys

#Relative import
sys.path.append("..")
from classes import Player, CPU, Table
from src.lenguages import lenguages
from functions.clear_display import clearDisplay

class Menu():
    def __init__(self):
        self.leng = ""
        self.mode = ""
        clearDisplay()
        self.changeLenguage()
        self.lobby()

    def changeLenguage(self):
        #Input for selecting a lenguage
        leng_selected = input(lenguages["start"]).lower()

        try:
            #Checks if the input issuitable
            lenguages[leng_selected]
            self.leng = leng_selected
        except KeyError:
            print(f"{leng_selected} is out of range, please select again / {leng_selected} esta fuera de rango, porfavor seleccione de nuevo")
            return self.changeLenguage()
    
    def toPlay(self):
        def singlePlayer():
            clearDisplay()
            Player.gamemode = "Singleplayer"
            print("Singleplayer")
            cpu_wanted = input(lenguages[self.leng]["menu"]["toPlay"]["ask"]).strip()

            try:
                cpu_wanted = int(cpu_wanted)
            except:
                print(f"{cpu_wanted}" + lenguages[self.leng]["menu"]["toPlay"]["error2"])
                return singlePlayer()

            if cpu_wanted <= 3 and cpu_wanted >= 1:
                for _ in range(cpu_wanted):
                    CPU()
                Player("Main Player")
                return
            else:
                print(f"{cpu_wanted}" + lenguages[self.leng]["menu"]["toPlay"]["error"])
                return singlePlayer()

        def multPlayer():
            clearDisplay()
            Player.gamemode = "Multiplayer"
            print("Multiplayer")
            players_wanted = input(lenguages[self.leng]["menu"]["toPlay"]["ask2"])
            cpu_wanted = input(lenguages[self.leng]["menu"]["toPlay"]["ask"])

            try:
                cpu_wanted = int(cpu_wanted)
                players_wanted = int(players_wanted)
            except:
                print(lenguages[self.leng]["menu"]["toPlay"]["error"])
                return multPlayer()
            
            if cpu_wanted + players_wanted <= 4 and players_wanted >= 2:
                for _ in range(players_wanted):
                    Player(input(f"Name of the player number {len(Player.player_list) + 1} "))
                for _ in range(cpu_wanted):
                    CPU()
            else:
                print(lenguages[self.leng]["menu"]["toPlay"]["error"])
                multPlayer()
        #Changes a class variable for using the same lenguage across other modules

        Player.leng = self.leng
        Table.leng = self.leng
        clearDisplay()

        #Selects the game mode (Singleplayer or Multiplayer)
        choice = input(lenguages[self.leng]["menu"]["toPlay"]["ask3"]).lower()
        
        try:
            choice = int(choice)
            try:
                choice = lenguages[self.leng]["menu"]["toPlay"]["gamemodes"][choice]
            except:
                print(lenguages[self.leng]["menu"]["toPlay"]["error"])
                return self.lobby()
        except:
            try:
                lenguages[self.leng]["menu"]["toPlay"]["gamemodes"][choice]
            except:
                print(lenguages[self.leng]["menu"]["toPlay"]["error"])
                return self.lobby()

        if choice == lenguages[self.leng]["menu"]["toPlay"]["gamemodes"][0]:
            return singlePlayer()
        elif choice == lenguages[self.leng]["menu"]["toPlay"]["gamemodes"][1]:
            return multPlayer()
        else:
            return self.lobby()
    
    def toHelp(self):
        clearDisplay()
        print(lenguages[self.leng]["menu"]["howtoplay"])
        input(lenguages[self.leng]["menu"]["help_exit_message"])
        return self.lobby()

    def toExit(self):
        clearDisplay()
        print(lenguages[self.leng]["menu"]["exit_message"])
        return exit()

    def lobby(self):
        clearDisplay()
        choice = input(lenguages[self.leng]["menu"]["lobby"]["input"])
        try:
            choice = int(choice)
            choice = lenguages[self.leng]["menu"]["lobby"]["choices"][choice]
        except:
            choice.lower()
        
        #Play
        if choice == lenguages[self.leng]["menu"]["lobby"]["choices"][0]:
            print("play!")
            return self.toPlay()
        #How to play
        elif choice == lenguages[self.leng]["menu"]["lobby"]["choices"][1]:
            return self.toHelp()
        #Exit
        elif choice == lenguages[self.leng]["menu"]["lobby"]["choices"][2]:
            return self.toExit()
        #User didn't choose any
        else:
            self.lobby()
        



if __name__ == "__main__":
    pass