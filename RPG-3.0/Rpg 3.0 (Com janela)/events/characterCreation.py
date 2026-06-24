from ui.effects import *
from systems import paths
from entities.player import Player
from configs import InitialPlayerLevel
import entities.monsters.early as earlyGame

def CharacterCreation():
    WindowClear()

    def AskFirstName():  # Ask first name
        InputPrompt("Change your character's first name: ", AskLastName)

    def AskLastName(FirstName):  # Ask last name
        if FirstName:
            InputPrompt("Change your character's last name: ", lambda LastName: ConfirmName(LastName, FirstName))
        else:
            AskFirstName()
    
    def ConfirmName(LastName, FirstName):  # Confirm full name
        if LastName:
            CharacterName = f"{FirstName} {LastName}"
            chosePath(CharacterName)
        else:
            AskLastName(FirstName)
        
    def chosePath(CharacterName):  # Choose character path
        WindowClear()

        frame = Frame(window)
        frame.pack(expand=True, pady=10)

        MainText("Choose your character's path:", frame)

        for i, path in enumerate(paths.PathsList, start=1):
            def chose(p=path):
                createPlayer(CharacterName, p)
            Button(frame, text=f"{i}. {path.name}", command=chose).pack(pady=5)

    def createPlayer(CharacterName, chosen_path):  # Create player with chosen path
        WindowClear()

        player = Player(CharacterName, InitialPlayerLevel, chosen_path)

        player.path = chosen_path
        player.status.sorcery += chosen_path.sorcery
        player.status.strength += chosen_path.strength
        player.status.resistance += chosen_path.resistance
        player.status.armorClass += chosen_path.armorClass
        player.status.agility += chosen_path.agility
        player.status.maxHp = player.status.CalcMaxHp()
        player.status.hp = player.status.maxHp

        StatusView(player, player.combat.Fight, (player, earlyGame.goblin))

    AskFirstName()