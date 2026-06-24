import systems.skills as skill

class Paths:
    def __init__(self, name, sorcery, strength, resistance, agility, armorClass, skills):
        self.name = name
        self.sorcery = sorcery
        self.strength = strength
        self.resistance = resistance
        self.agility = agility
        self.armorClass = armorClass
        self.skills = skills

    def __str__(self):
        return f"{self.name}"
    
# -----------------------------------   Paths    -----------------------------------

# Example = Paths(name, sorcery, strength, resistance, agility, armorClass)

Mage = Paths("Mage", 3, 0, 0, 0, 0, [skill.fireball, skill.iceSpike, skill.magicMissile, skill.push])
MagicSwordman = Paths("Magic Swordman", 1, 1, 1, 1, 2, [skill.lunge, skill.iceSpike, skill.push, skill.magicMissile])
Warrior = Paths("Warrior", 0, 2, 1, 1, 2, [skill.lunge, skill.swordSlash, skill.powerStrike, skill.push])
Paladin = Paths("Paladin", 0, 1, 2, 1, 3, [skill.smite, skill.powerStrike, skill.swordSlash, skill.push])
Tinkerer = Paths("Tinkerer", 1, 0, 1, 2, 1, [skill.push, skill.lunge, skill.powerStrike, skill.iceSpike])

# List of all Paths
List = [
    value
    for value in globals().values()
    if isinstance(value, Paths)
]
