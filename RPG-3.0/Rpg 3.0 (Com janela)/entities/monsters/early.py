import systems.skills as skill
from entities.monster import Monster

goblin = Monster(
    name = "Goblin", 
    level = 1, 
    skills = [skill.lunge, skill.push],
    xp = 50
    )
wolf = Monster(
    name = "Wolf", 
    level = 3, 
    skills = [skill.bite, skill.scratch],
    xp = 100
    )