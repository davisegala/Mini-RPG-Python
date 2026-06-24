class Item:
    def __init__(self, name, 
                function=None, 
                value=0, 
                description="This item does something useful.", 
                healAmount=0,
                statusGain=None, # This input should be a list of tuples (statusName, increaseAmount)
                ):

        self.name = name
        self.function = function
        self.value = value
        self.description = description
        self.healAmount = healAmount
        self.statusGain = statusGain

    def heal(self, target):
        target.status.hp += self.healAmount
        if target.status.hp > target.status.maxHp:
            target.status.hp = target.status.maxHp

    def boostStatus(self, target):
       if self.statusGain:
           for statusName, increaseAmount in self.statusGain:
               target.status.__dict__[statusName] += increaseAmount
    
# ------------------------------------   Items    -----------------------------------

HealthPotion = Item(
    name="Health Potion",
    function="heal",
    value=10,
    description="A potion that restores 30 HP.",
    healAmount=30
)