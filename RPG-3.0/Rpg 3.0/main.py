from events.characterCreation import CharacterCreation
from entities.monster import Monster
import systems.skills as skills
import entities.monsters.early as earlyGame

#StartingGame()

player = CharacterCreation(1)  # initial level

player.combat.Fight(player, earlyGame.goblin)