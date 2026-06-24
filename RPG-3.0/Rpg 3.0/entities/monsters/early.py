import systems.skills as skill
from entities.monster import Monster

goblin = Monster("Goblin", 1, skills=[skill.lunge, skill.push])
wolf = Monster("Wolf", 3, [skill.bite])