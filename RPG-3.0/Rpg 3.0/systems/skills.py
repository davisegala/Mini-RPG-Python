class Skills:
    def __init__(self, name, base_damage, atribute, cost, cooldown, description):
        self.name = name
        self.base_damage = base_damage
        self.atribute = atribute
        self.cost = cost
        self.cooldown = cooldown
        self.description = description

    def calcDamage(self, user, skill, target):
        if skill.atribute == "sorcery":
            damage = skill.base_damage + (user.status.sorcery * 3)
        elif skill.atribute == "strength":
            damage = skill.base_damage + (user.status.strength * 2)
        else:
            damage = skill.base_damage
        damage = damage - (target.status.armorClass * 1.5)
        if damage < 0:
            damage = 0
        return int(damage)
    
    # make a method to verify if the skill can be used (enough mana, not in cooldown, etc)

# -----------------------------------   Skills    -----------------------------------

# Example = Skills(name, base damage, atribute, cost, cooldown, description)

push = Skills("Push", 10, "strength", 0, 1, "A strong push that deals light damage and may stagger the enemy.")
lunge = Skills("Lunge", 15, "strength", 0, 2, "A powerful forward thrust dealing moderate damage.")
fireball = Skills("Fireball", 25, "sorcery", 10, 3, "A fiery projectile that explodes upon impact, dealing high damage.")
magicMissile = Skills("Magic Missile", 15, "sorcery", 7, 2, "A homing magical projectile that never misses its target.")
iceSpike = Skills("Ice Spike", 20, "sorcery", 9, 3, "Launches a sharp icicle at the enemy, dealing damage and slowing them down.")
swordSlash = Skills("Sword Slash", 15, "strength", 0, 2, "A quick slash with a sword that deals moderate damage.")
powerStrike = Skills("Power Strike", 30, "strength", 0, 4, "A heavy strike that deals significant damage to a single target.")
smite = Skills("Smite", 28, "sorcery", 11, 4, "Calls down a holy light to strike the enemy, dealing high damage.")

# Monsters skills

bite = Skills("Bite", 10, "strength", 0, 0, "")
scratch = Skills("Scratch", 7, "strenght", 0, 0, "")