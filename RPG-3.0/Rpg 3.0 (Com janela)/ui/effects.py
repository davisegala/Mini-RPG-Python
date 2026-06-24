import os
import time
from tkinter import *
from ui.app import window

#terminal effect

def ClearTerminal():
    os.system("cls" if os.name == "nt" else "clear")

# interface effects

def WindowClear():
    for widget in window.winfo_children():
        widget.destroy()

def WindowTransition(timeDelay = 1):
    time.sleep(timeDelay)
    WindowClear()

def MainText(text, frame=window):
    mainText = Label(frame, text=text)
    mainText.pack(anchor="center") 

def InputPrompt(text, callback):
    MainText(text)

    frame = Frame(window)
    frame.pack()

    text_var = StringVar()
    entry = Entry(frame, textvariable=text_var)
    entry.pack(side="left")

    def confirm():
        value = text_var.get().strip()
        WindowClear()
        callback(value)
       
    Button(frame, text="OK", command=confirm).pack(side="right")

def StatusView(entity, next=lambda: None, args=()):
    WindowClear()

    MainText(
        f"Character Created!\n\n"
        f"Name: {entity.name}\n"
        f"Path: {entity.path.name}\n"
        f"Level: {entity.level}\n\n"
        f"Stats:\n"
        f"HP: {entity.status.hp}/{entity.status.maxHp}\n"
        f"Strength: {entity.status.strength}\n"
        f"Sorcery: {entity.status.sorcery}\n"
        f"Resistance: {entity.status.resistance}\n"
        f"Armor Class: {entity.status.armorClass}\n"
        f"Agility: {entity.status.agility}"
    )

    frame = Frame(window)
    frame.pack(pady=10)

    Button(frame, text="Close", command=lambda: next(*args)).pack()
