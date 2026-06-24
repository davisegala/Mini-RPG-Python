import os
import time

def ClearTerminal():
    os.system("cls" if os.name == "nt" else "clear")

def ScreenTransition(timeDelay = 1):
    time.sleep(timeDelay)
    ClearTerminal()

def YesOrNot(question):
    choice = input(question).strip().lower()
    return choice