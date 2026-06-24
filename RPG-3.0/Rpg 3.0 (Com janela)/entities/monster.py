from systems.status import Status
from systems.level import Level
import systems.combat as combat
import systems.skills as skill

class Monster:
    def __init__(self, name="NoName", level=1, xp=0, skills=[]):
        self.name = name
        self.status = Status()
        self.level = Level(level, self.status)
        self.skills = skills
        self.xp = xp
        self.combat = combat.Combat()