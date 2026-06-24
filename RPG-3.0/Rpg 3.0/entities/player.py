from systems.status import Status
from systems.level import Level
from systems.paths import Paths
from systems.combat import Combat

class Player:
    def __init__(self, name, level, path):
        self.name = name
        self.status = Status()
        self.level = Level(level, self.status)
        self.path = path
        self.combat = Combat()
        self.skills = path.skills