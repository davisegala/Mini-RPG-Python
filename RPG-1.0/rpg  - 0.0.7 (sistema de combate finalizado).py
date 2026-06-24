import random

def monster_atk(hp, m): #ataques dos monstros
    matk = random.randint(1, 17)
    if matk > 5:
        print(f'{m} lança um ataque...')
        print(f'{m} acertou o ataque | [-11 hp]')
        hp -= 11
    elif matk < 5:
        print(f'{m} lança um ataque...')
        print(f'{m} errou o ataque')
    else:
        print(f'{m} lança um ataque...')
        print(f'{m} acertou um... ATAQUE CRÍTICO! | [-19 hp]')
        hp -= 19
    return hp

def player_atk_mage(mhp, hp, dano, selecao): #ataques dos players magos
    if selecao == 'magic-missile':
        mhp -= dano  
        print(f'{m} recebeu {dano} de dano | [{mhp} hp]')
    elif selecao == 'heal':
        hp += 14
        hp = min(hp, 30)
        print(f'Seu hp é {hp}')
    elif selecao == 'frozen':
        mhp -= dano - 1
        print(f'{m} recebeu {dano - 1} de dano | [{mhp} hp]')
    else:
        print('Você errou a conjuração | [-9 hp]')
        hp -= 9
    return hp, mhp

def player_atk_warrior(mhp, hp, dano, selecao): #ataques dos players guerreiros
    if selecao == 'small-cut':
        mhp -= dano
        print (f'{m} recebeu {dano} de dano [{mhp} hp]')
    elif selecao == 'fortification':
        dano += 3
        dano = min(20, dano)
        print(f'Seu hp é {hp}')
    elif selecao == 'lunge':
        mhp -= dano - 1
        print (f'{m} recebeu {dano} de dano [{mhp} hp]')
    else:
        print(f'{nome} errou o nome do movimento | [-9 hp]')
        hp -= 9
    return hp, mhp
    
class player_info:
    def __init__(self, nome, xp, classe, status):
        self.nome = nome
        self.xp = xp
        self.classe = classe
        self.status = status


    
start = input("Start? [Y/N]\n").lower()
if start == "y":
    print("***************************************")
    nome = input("Defina um nick: ")
else:
    print("***************************************")
    exit()

classe = input("Escolha uma classe entre [1] para Mago e [2] para Guerreiro\n")
if classe == "1":
    magia, forca, hp = random.randint(5, 7), random.randint(1, 2), 30
    dano = magia + 3
elif classe == "2":
    magia, forca, hp = random.randint(1, 2), random.randint(5, 7), 45
    dano = forca + 3
else:
    print("Classe inválida. Saindo...")
    exit()
status = magia, forca, hp
xp = 0
print("***************************************")
print(f"Seus status são: Magia {magia}/Força {forca}/Vida {hp}")
print("***************************************")

# Monstro
m, mhp = random.choice([("goblin", 17), ("javali", 15)])

# --------------------------------------------------------------------- Primeiro combate -----------------------------------------------------------------------------

print(f'{nome} encontrou uma criatura...')
print(f'É um... {m} | [{mhp}]')
print(player_info.xp)
# Ataques
while mhp > 0 and hp > 0:  # Sistema de combate
    
    if classe == '1':
        selecao = input('Selecione o ataque [Magic-Missile|Heal|Frozen] \n').lower()
        hp, mhp = player_atk_mage(mhp, hp, dano, selecao)
        
        if mhp > 0:  # O monstro ataca apenas se ainda estiver vivo
            hp = monster_atk(hp, m)

        print(f'-----HP do jogador: [{hp}], HP do monstro: [{mhp}]-----')
            
    if classe == '2':
        selecao = input('Selecione o ataque [Small-Cut|Fortification|Lunge] \n')
        hp, mhp = player_atk_warrior(mhp, hp , dano, selecao)

        if mhp > 0:  # O monstro ataca apenas se ainda estiver vivo
            hp = monster_atk(hp, m)

        print(f'-----HP do jogador: [{hp}], HP do monstro: [{mhp}]-----')

        
if mhp <= 0:
    xp = random.randint(10, 20)
    print(f'--Parabéns! {nome} venceu um {m} e ganhou [{xp} xp]')
else:
    print(f'{nome} foi derrotado por {m}...')
    exit()

# Fim do primeiro sistema de combate
