import random

def monster_atk(hp, m):  # Ataques dos monstros
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

def player_atk_mage(mhp, hp, dano, selecao, m):  # Ataques dos players magos
    if selecao == 'magic-missile':
        mhp -= dano
        print(f'{m} recebeu {dano} de dano | [{mhp} hp]')
    elif selecao == 'heal':
        hp += 14
        hp = min(hp, max_hp)
        print(f'Seu hp é {hp}')
    elif selecao == 'frozen':
        mhp -= dano - 1
        print(f'{m} recebeu {dano - 1} de dano | [{mhp} hp]')
    elif selecao == 'skip':
        mhp = 0
    else:
        print('Você errou a conjuração | [-9 hp]')
        hp -= 9
        
    return hp, mhp

def player_atk_warrior(mhp, hp, dano, selecao, m):  # Ataques dos players guerreiros
    if selecao == 'small-cut':
        mhp -= dano
        print(f'{m} recebeu {dano} de dano [{mhp} hp]')
    elif selecao == 'fortification':
        hp += 5
        hp = min(hp, max_hp)
        print(f'Seu hp é {hp}')
    elif selecao == 'lunge':
        mhp -= dano - 1
        print(f'{m} recebeu {dano} de dano [{mhp} hp]')
    else:
        print(f'{nome} errou o nome do movimento | [-9 hp]')
        hp -= 9
    return hp, mhp, dano

def player_info(nome, hp, magia, forca, classe, level, xp):  # Informações sobre o player
    print('==================================================================')
    print(f'            Status: Magia {magia}, Força {forca}, Vida {hp}')
    print(f'            Nome: {nome}     |     Classe: {classe2}')
    print(f'            Level: {level}   |     Xp: {xp}')
    print('==================================================================')

def painel(nome, hp, mhp, pxp, magia, forca, classe, level, xp): 
    painel = input(f'O que deseja fazer? Digite [help] para ver as opções \n')
    if painel == 'help':
        print('[status] : usado para ver as informações do player')
        print('[hunter] : usado caso o jogador queira caçar monstros')
    elif painel == 'status':
        player_info(nome, hp, magia, forca, classe, level, xp)
    elif painel == 'hunter':
        hp, mhp, pxp, xp = combate(hp, mhp, dano, classe, nome, pxp)
    return hp, mhp, xp, pxp

def xp_sytem(pxp, level):  # Sistema de XP
    if pxp > 0 and pxp < 50:
        level = 1
    elif pxp > 50 and pxp < 125:
        level = 2
    return level

def mage_atk(hp, mhp, dano, m):  # Ataque do mago
    while mhp > 0 and hp > 0:
        selecao = input('Selecione o ataque [Magic-Missile|Heal|Frozen] \n').lower()
        hp, mhp = player_atk_mage(mhp, hp, dano, selecao, m)
        if mhp > 0: 
            hp = monster_atk(hp, m)
        print(f'-----HP do jogador: [{hp}], HP do monstro: [{mhp}]-----')
    print(' ')
    print('----------------------FIM DO COMBATE----------------------')
    print(' ')
    return hp, mhp

def warrior_atk(hp, mhp, dano, m):  # Ataque do guerreiro
    while mhp > 0 and hp > 0:
        selecao = input('Selecione o ataque [Small-Cut|Fortification|Lunge] \n').lower()
        hp, mhp = player_atk_warrior(mhp, hp, dano, selecao, m)
        if mhp > 0: 
            hp = monster_atk(hp, m)
        print(f'-----HP do jogador: [{hp}], HP do monstro: [{mhp}]-----')
    print(' ')
    print('----------------------FIM DO COMBATE----------------------')
    print(' ')
    return hp, mhp

def combate(hp, mhp, dano, classe, nome, pxp):  # Função de combate
    if classe == '1':
        hp, mhp = mage_atk(hp, mhp, dano, m)
    elif classe == '2':
        hp, mhp = warrior_atk(hp, mhp, dano, m)
    if mhp <= 0:
        xp = random.randint(10, 20)
        pxp = pxp + xp
        print(f'--Parabéns! {nome} venceu um {m} e ganhou [{xp} xp]')
    else:
        print(f'{nome} foi derrotado por {m}...')
        exit()
    return hp, mhp, pxp, xp

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

start = input("Start? [Y/N]\n").lower()
print(' ')
if start == "y":
    print("***************************************")
    print(' ')
    nome = input("Defina um nick: ")
else:
    print("***************************************")
    exit()
print(' ')
print('Nesse jogo todas as respostas devem ser escritas em letras')
print('minusculas e (se necessário) usando "-"')
print(' ')

classe = input("Escolha uma classe entre [1] para Mago e [2] para Guerreiro\n")
if classe == "1":
    magia, forca, hp, max_hp = random.randint(5, 7), random.randint(1, 2), 30, 30
    dano = magia + 3
    classe2 = 'mago'
elif classe == "2":
    magia, forca, hp, max_hp = random.randint(1, 2), random.randint(5, 7), 45, 45
    dano = forca + 3
    classe2 = 'guerreiro'
else:
    print("Classe inválida. Saindo...")
    exit()

xp = 0
level = 1
pxp = 0

print("***************************************")
print(f"Seus status são: Magia {magia}/Força {forca}/Vida {hp}")
print("***************************************")

# --------------------------------------------------------------------- Primeiro combate -----------------------------------------------------------------------------
m, mhp = random.choice([("goblin", 17), ("javali", 15)])
print(f'{nome} encontrou uma criatura...')
print(f'É um... {m} | [{mhp}]')
print(' ')

hp, mhp, pxp, xp = combate(hp, mhp, dano, classe, nome, pxp)
      
hp, mhp, xp, pxp = painel(nome, hp, pxp, mhp, magia, forca, classe, level, xp)

hp, mhp, xp, pxp = painel(nome, hp, mhp, pxp, magia, forca, classe, level, xp)

# Fim do primeiro sistema de combate
