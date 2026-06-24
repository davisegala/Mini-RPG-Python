class Status:
    def __init__(self):
        self.sorcery = 1
        self.strength = 1
        self.resistance = 1
        self.agility = 1
        self.armorClass = 0
        self.maxHp = self.CalcMaxHp()
        self.hp = self.maxHp

    def CalcMaxHp(self):
        return 40 + (self.resistance * 10)

    def StatsLevelUp(self):
        self.sorcery += 1
        self.strength += 1
        self.resistance += 1
        self.agility += 1
        self.maxHp = self.CalcMaxHp()
        self.hp = self.maxHp
