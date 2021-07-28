import os

def clearDisplay():
    #This will be True if the user is in Windows.
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")