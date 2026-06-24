from ui.effects import *
from systems.skills import *
import tkinter as tk
import random

# fazer um metodo para quando usar uma skill voltar para o menu de ações
# fazer o inventario
# fazer a função de correr

class Combat:
    def SetupUI(self):
        WindowClear()

        self.mainFrame = Frame(window)
        self.mainFrame.pack(expand=True, fill="both", pady=10)

        self.statusLabel = Label(self.mainFrame, text="", font=("Arial", 10))
        self.statusLabel.pack(pady=5)

        self.messageLabel = Label(self.mainFrame, text="", font=("Arial", 10))
        self.messageLabel.pack(pady=10)

        self.skillsFrame = Frame(self.mainFrame)
        self.skillsFrame.pack(pady=10)

        self.menuFrame = Frame(window)
        self.menuFrame.pack(side="bottom", pady=40)

    def ShowFightStatus(self):
        self.statusLabel.config(
            text=(
                f"Player HP: {self.player.status.hp}/{self.player.status.maxHp}\n"
                f"{self.enemy.name} HP: {self.enemy.status.hp}/{self.enemy.status.maxHp}"
            )
        )

    def MenuCombat(self):
        for widget in self.menuFrame.winfo_children():
            widget.destroy()

        inventory = tk.Button(self.menuFrame, text="Inventory")
        attack = tk.Button(self.menuFrame, text="Attack", command=self.PlayerSelectSkill)
        escape = tk.Button(self.menuFrame, text="Run", command=self.Run)

        inventory.pack(side="left", padx=10)
        attack.pack(side="left", padx=10)
        escape.pack(side="left", padx=10)

    def ShowMessage(self, text):
        self.messageLabel.config(text=text)

    def CheckEnd(self):
        if self.player.status.hp <= 0:
            MainText("You die")
            WindowTransition(3)
            window.quit()
            return True
        elif self.enemy.status.hp <= 0:
            WindowClear()
            MainText(f"{self.enemy.name} has been defeated")
            self.player.level.XpGain(self.enemy.xp)
            self.onEnd()
            return True
        
    def SwitchTurn(self):
        self.attacker, self.defender = self.defender, self.attacker
        
    def CalcDamage(self, user, target, skill):
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
    
    def MissCheck(self, user, target):
        hitChance = 100 - (target.status.agility * 2) + (user.status.agility)
        hitChance = max(5, min(95, hitChance))
        roll = random.randint(1, 100)
        return roll <= hitChance
    
    def AfterAttack(self):
        if self.CheckEnd():
            return

        self.SwitchTurn()
        self.NextTurn()
    
    def UseSkill(self, user, target, skill):
        self.playerTurn = False
        if self.MissCheck(user, target):
            damage = self.CalcDamage(user, target, skill)
            target.status.hp -= damage
            if target.status.hp < 0:
                target.status.hp = 0
            self.ShowMessage(
                f"{user.name} used {skill.name} on {target.name}, dealing {damage} damage!"
            )
        else:
            self.ShowMessage(
                f"{user.name} used {skill.name} on {target.name}, but missed!"
            )

        self.ShowFightStatus()
        window.after(1200, self.AfterAttack)

    def PlayerTurnVerify(self, user, target, skill):
        if self.playerTurn:
            self.UseSkill(user, target, skill) 

    def FirstTurn(self, entity1, entity2):
        if entity1.status.agility > entity2.status.agility:
            return entity1, entity2
        elif entity2.status.agility > entity1.status.agility:
            return entity2, entity1
        else:
            return random.choice([(entity1, entity2), (entity2, entity1)])
    
    def NextTurn(self):
        if self.attacker == self.player:
            self.PlayerTurn()
        else:
            self.EnemyTurn()

    def PlayerSelectSkill(self):
        for widget in self.skillsFrame.winfo_children():
            widget.destroy()

        Label(self.skillsFrame, text="Select a skill to use:").pack(pady=5)

        for skill in self.player.skills:
            Button(
                self.skillsFrame,
                text=skill.name,
                command=lambda s=skill: self.PlayerTurnVerify(self.player, self.enemy, s)
            ).pack(pady=3)

    def Run(self):
        WindowClear()
        MainText("Error...")

    def PlayerTurn(self):
        self.playerTurn = True
        self.MenuCombat()

    def EnemyTurn(self):
        skill = random.choice(self.enemy.skills)
        self.UseSkill(self.enemy, self.player, skill)

    def Fight(self, player, enemy, onEnd=lambda: None):
        self.player = player
        self.enemy = enemy
        self.onEnd = onEnd

        self.SetupUI()
        self.ShowFightStatus()

        self.attacker, self.defender = self.FirstTurn(player, enemy)
        self.NextTurn()