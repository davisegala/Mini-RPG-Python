from effects import *

def StartingGame():
    while True:
        ClearTerminal()
        choice = YesOrNot("Start [Y/N]\n")
        ScreenTransition()
        if choice == "y":
            return
        elif choice == "n":
            exit()