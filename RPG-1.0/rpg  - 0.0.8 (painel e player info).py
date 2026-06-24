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
    elif selecao == 'skip':
        mhp = 0
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
    
def player_info(nome, hp, magia, forca, classe, level, xp): #informaçoes sobre o player
    print('==================================================================')
    print(f'    Seus status são: Magia {magia}, Força {forca}, Vida {hp}')
    print(f'            Nome: {nome}     |     Classe: {classe2}  |
    print(f'            Level: {level}   |     Xp: {xp}')
    print('==================================================================')

def painel(player_info): 
    painel = input(f'O que deseja fazer? Digite [help] para ver as opções \n')
    if painel == 'help':
        print('[status] : usado para ver as informações do player')
    elif painel == 'status':
        player_info = player_info(nome, hp, magia, forca, classe, level, xp)

def xp_sytem(xp, level, pxp):
    if pxp > 0 and pxp < 50:
        level = 1
    elif pxp > 50 and pxp < 125:
        level = 2
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
print('minusculas e (se necessario) usando "-"')
print(' ')

classe = input("Escolha uma classe entre [1] para Mago e [2] para Guerreiro\n")
if classe == "1":
    magia, forca, hp = random.randint(5, 7), random.randint(1, 2), 30
    dano = magia + 3
    classe2 = 'mago'
elif classe == "2":
    magia, forca, hp = random.randint(1, 2), random.randint(5, 7), 45
    dano = forca + 3
    classe2 = 'guerreiro'
else:
    print("Classe inválida. Saindo...")
    exit()
    
xp = 0
level = 1

print("***************************************")
print(f"Seus status são: Magia {magia}/Força {forca}/Vida {hp}")
print("***************************************")

# Monstro
m, mhp = random.choice([("goblin", 17), ("javali", 15)])

# --------------------------------------------------------------------- Primeiro combate -----------------------------------------------------------------------------
resposta = input(f'Deseja um tutorial basico sobre o combate? [Y/N] \n')
if resposta == 'y':
    print() # fazer o tutorial basico                                                                                           !!!
print(' ')

print(f'{nome} encontrou uma criatura...')
print(f'É um... {m} | [{mhp}]')
print(' ')
# Ataques
while mhp > 0 and hp > 0:  # Sistema de combate
    
    if classe == '1':
        selecao = input('Selecione o ataque [Magic-Missile|Heal|Frozen] \n').lower()
        hp, mhp = player_atk_mage(mhp, hp, dano, selecao)
        
        if mhp > 0: 
            hp = monster_atk(hp, m)

        print(f'-----HP do jogador: [{hp}], HP do monstro: [{mhp}]-----')
            
    if classe == '2':
        selecao = input('Selecione o ataque [Small-Cut|Fortification|Lunge] \n')
        hp, mhp = player_atk_warrior(mhp, hp , dano, selecao)

        if mhp > 0:  
            hp = monster_atk(hp, m)

        print(f'-----HP do jogador: [{hp}], HP do monstro: [{mhp}]-----')

        
if mhp <= 0:
    xp = random.randint(10, 20)
    pxp = pxp + xp
    print(f'--Parabéns! {nome} venceu um {m} e ganhou [{xp} xp]')
    
else:
    print(f'{nome} foi derrotado por {m}...')
    exit()

painel(player_info)

# Fim do primeiro sistema de combate
