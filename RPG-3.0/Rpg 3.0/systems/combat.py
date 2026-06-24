from ui.effects import *
from systems.skills import *
import random

class Combat:  
    def missCheck(self, user, target):
        hitChance = 100 - (target.status.agility * 2) + (user.status.agility)
        roll = random.randint(1, 100)
        return roll <= hitChance
    
    def useSkill(self, user, target, skill):
        damage = skill.calcDamage(user, skill, target)
        if damage > 0 and self.missCheck(user, target) and skill in user.skills:
            target.status.hp -= damage
            if target.status.hp < 0:
                target.status.hp = 0
            print(f"{user.name} used {skill.name} on {target.name}, dealing {damage} damage!")
        else:
            print(f"{user.name} used {skill.name} on {target.name}, but it missed!")

        ScreenTransition(3)

    def FirstTurn(self, entity1, entity2):
        if entity1.status.agility > entity2.status.agility:
            return entity1
        elif entity2.status.agility > entity1.status.agility:
            return entity2
        else:
            return random.choice([entity1, entity2])
        
    def Fight(self, player, entity):
        attacker = self.FirstTurn(player, entity)
        defender = entity if attacker == player else player

        while player.status.hp > 0 and entity.status.hp > 0:
            ScreenTransition(2)
            print(f"Player HP: {player.status.hp}/{player.status.maxHp}")
            print(f"{entity.name} HP: {entity.status.hp}/{entity.status.maxHp}\n")
            # Attacker's turn
            if attacker == player:
                skill = self.PlayerSelectSkill(player)
            else:
                skill = random.choice(entity.skills)
            
            self.useSkill(attacker, defender, skill)
            
            # Check if defender is defeated
            if defender.status.hp <= 0:
                print(f"{defender.name} has been defeated!")
                break

            # Swap roles
            attacker, defender = defender, attacker
        
    def PlayerSelectSkill(self, player):
        while True:
            print("Select a skill to use:")
            for idx, skill in enumerate(player.skills):
                print(f"{idx + 1}. {skill.name} - {skill.description} (Cost: {skill.cost} Mana)")

            choice = int(input("Enter the number of the skill: ")) - 1
            if 0 <= choice < len(player.skills):
                return player.skills[choice]
            else:
                print("Invalid choice. Defaulting to first skill.")
                ClearTerminal()