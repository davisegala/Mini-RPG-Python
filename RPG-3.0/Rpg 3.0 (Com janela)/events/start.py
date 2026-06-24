from ui.effects import *
from tkinter import *
from ui.app import window
from events.characterCreation import CharacterCreation

def StartingGame():
    MainText("Welcome to the RPG Game!")
    frame = Frame(window)
    frame.pack(expand=True, pady=10)

    # Start button inside the frame
    start = Button(frame, text="Start Game", command=lambda: CharacterCreation())
    start.pack(padx=5, pady=5, side="left")

    # Exit button inside the frame
    exit = Button(frame, text="Exit", command=window.quit)
    exit.pack(padx=5, pady=5, side="right")