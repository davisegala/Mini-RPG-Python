class Level:
    def __init__(self, level, status):
        self.xp = 0
        self.metaXp = 500
        self.level = level
        self.status = status

        for _ in range(level - 1):
            self.metaXp = int(self.metaXp * 1.5)
            self.status.StatsLevelUp()

    def metaXpCalc(self):
        self.metaXp *= 1.5
        self.metaXp = int(self.metaXp)
        return self.metaXp

    def LevelCalc(self):
        upLevel = False
        while self.xp >= self.metaXp:
            self.level += 1
            self.status.StatsLevelUp()
            self.metaXp = self.metaXpCalc()
            upLevel = True
        return upLevel
    
    def XpGain(self, amount):
        self.xp += amount
        upLevel = self.LevelCalc()

        if upLevel:
            print(f"Leveled up! Now level {self.level}")
        else:
            print(f"Gained {amount} XP. Current XP: {self.xp}/{self.metaXp}")
