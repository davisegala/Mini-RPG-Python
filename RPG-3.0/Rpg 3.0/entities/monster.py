from systems.status import Status
from systems.level import Level
import systems.combat as combat

class Monster:
    def __init__(self, name, level, skills):
        self.name = name
        self.status = Status()
        self.level = Level(level, self.status)
        self.skills = skills
        self.combat = combat.Combat()