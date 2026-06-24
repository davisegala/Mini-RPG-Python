from ui.effects import *
from systems import paths
from entities.player import Player

def CharacterCreation(initialLevel):
    # Character Name
    while True:
        ScreenTransition()
        FirstName = input("Change your character's first name: ").strip()
        LastName = input("Change your character's last name: ").strip()
        CharacterName = f"{FirstName} {LastName}"

        choice = YesOrNot(f"Your character name is {CharacterName}? [Y/N]\n")
        ScreenTransition()
        if choice == "y":
            break
        elif choice != "y":
            print("Let's try again...")

    # Character Path
    while True:
        ScreenTransition()
        print("-- Available paths --")

        for i, path in enumerate(paths.List, start=1):
            print(f"[{i}] {path}")

        try:
            choice = int(input("Choose your path: "))
            if 1 <= choice <= len(paths.List):
                chosen_path = paths.List[choice - 1]
                break
            else:
                print("Invalid option.\n")
        except ValueError:
            print("Please type a number.\n")

    player = Player(CharacterName, initialLevel, chosen_path)

    player.status.sorcery += chosen_path.sorcery
    player.status.strength += chosen_path.strength
    player.status.resistance += chosen_path.resistance
    player.status.armorClass += chosen_path.armorClass
    player.status.agility += chosen_path.agility
    player.status.maxHp = player.status.CalcMaxHp()
    player.status.hp = player.status.maxHp

    return player