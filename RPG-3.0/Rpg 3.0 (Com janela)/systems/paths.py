import systems.skills as skill

class Paths:
    def __init__(self, name, sorcery=0, strength=0, resistance=0, agility=0, armorClass=0, skills=None):
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

Mage = Paths(name="Mage", 
    sorcery=3, 
    skills=[skill.fireball, skill.iceSpike, skill.magicMissile, skill.push]
    )

MagicSwordman = Paths(
    name="Magic Swordman", 
    sorcery=1, 
    strength=1, 
    resistance=1, 
    agility=1, 
    armorClass=2, 
    skills=[skill.lunge, skill.iceSpike, skill.push, skill.magicMissile]
    )

Warrior = Paths(
    name="Warrior", 
    strength=2, 
    resistance=1, 
    agility=1, 
    armorClass=2, 
    skills=[skill.lunge, skill.swordSlash, skill.powerStrike, skill.push]
    )

Paladin = Paths(
    name="Paladin", 
    strength=1, 
    resistance=2, 
    agility=1, 
    armorClass=3, 
    skills=[skill.smite, skill.powerStrike, skill.swordSlash, skill.push]
    )
Tinkerer = Paths(
    name="Tinkerer", 
    sorcery=1, 
    resistance=1, 
    agility=2, 
    armorClass=1, 
    skills=[skill.push, skill.lunge, skill.powerStrike, skill.iceSpike]
    )

# List of all Paths
PathsList = [
    value
    for value in globals().values()
    if isinstance(value, Paths)
]
