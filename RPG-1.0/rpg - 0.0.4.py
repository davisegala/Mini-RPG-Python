import random #random

start = input ("Start? [Y/N]\n")
if start == "y":
    print ("***************************************")
if start == "y":
    nome = input ("Defina um nick: ")
elif start == "n": ("***************************************")

magia = 0 #magia
forca = 0 #força
hp = 100 #velocidade

classe = input ("Escolha uma classe entre [1] para Mago e [2] para Guerreiro\n")
if classe == "1":
    magia = random.randint(5,7)
    forca = random.randint(1,2)
    hp = 30

elif classe == "2":
    magia = random.randint(1,2)
    forca = random.randint(5,7)
    hp = 45

print ("***************************************")

print (f"Seus status são: Magia {magia}/Força {forca}/Vida {hp}")

print ("***************************************")

#monstro

m = random.randint(1,2)
if m == 1:
    m = 'goblin'
    mhp = 17
elif m == 2:
    m = 'javali'
    mhp = 15

#primeiro combate

print ('Você encontrou uma criatura...')
print (f'É um... {m} | [{mhp}] de vida')

#ataques

while mhp > -1 or mhp == 0:
    if classe == '1':
        selecao = input('Selecione o ataque [Magic-Missile|Heal|Frozen] \n')
        if selecao == 'magic-missile':
            if magia == 5:
                mhp = mhp -  5
                dano = 5
            elif magia == 6:
                mhp = mhp - 6
                dano = 6
            elif magia == 7:
                mhp = mhp - 7
                dano = 7
            print (f'{m} recebeu {dano} de dano [{mhp} hp]')
        elif selecao == 'heal':
            hp = hp + 14
            if hp > 30:
                hp = 30
            print(f'Seu hp é {hp}')
        elif selecao == 'frozen':
            if magia == 5:
                mhp = mhp -  4
                dano = 4
            elif magia == 6:
                mhp = mhp - 5
                dano = 5
            elif magia == 7:
                mhp = mhp - 6
                dano = 6
            print (f'{m} recebeu {dano} de dano | [{mhp} hp]')
        else:
            print('você errou a conjuração | [-9 hp]')
            hp = hp - 9
    if classe == '2':
        selecao = input('Selecione o ataque [Small-Cut|Fortification|Lunge] \n')
        if selecao == 'small-cut':
            if forca == 5:
                mhp = mhp -  5
                dano = 5
            elif forca == 6:
                mhp = mhp - 6
                dano = 6
            elif forca == 7:
                mhp = mhp - 7
                dano = 7
            print (f'{m} recebeu {dano} de dano [{mhp} hp]')
        elif selecao == 'fortification':
            hp = hp + 14
            if hp > 30:
                hp = 30
            print(f'Seu hp é {hp}')
        elif selecao == 'lunge':
            if forca == 5:
                mhp = mhp -  4
                dano = 4
            elif forca == 6:
                mhp = mhp - 5
                dano = 5
            elif forca == 7:
                mhp = mhp - 6
                dano = 6
            print (f'{m} recebeu {dano} de dano [{mhp} hp]')
        else:
            print('você errou o nome do movimento | [-9 hp]')
            hp = hp - 9
    if mhp > 0:
        matk = random.randint(1,19)
        if matk > 10:
            print(m, 'lança um ataque...')
            print(f'{m} acertou o ataque | [-11 hp]')
            hp = hp - 11
        elif matk < 10:
            print(m, 'lança um ataque...')
            print(f'{m} errou o ataque')
        elif matk == 10:
            print(m, 'lança um ataque...')
            print(f'{m} acertou um... ATAQUE CRÍTICO! | [-19 hp]')
            hp = hp - 19

#fim do primeiro sistema de combate

        
    
