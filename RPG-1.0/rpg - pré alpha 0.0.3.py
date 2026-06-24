import random #random

start = input ("Start? [Y/N]\n")
if start == "y":
    print ("***************************************")
if start == "y":
    nome = input ("Defina um nick: ")
elif start == "n": ("***************************************")

m = 0 #magia
f = 0 #força
hp = 100 #velocidade

classe = input ("Escolha uma classe entre [1] para Mago e [2] para Guerreiro\n")
if classe == "1":
    m = random.randint(5,7)
    f = random.randint(1,2)
    hp = 80

elif classe == "2":
    m = random.randint(1,2)
    f = random.randint(5,7)
    hp = 100

print ("***************************************")

print (f"Seus status são: Magia {m}/Força {f}/Vida {hp}")

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
print (f'É um... {m} com {mhp} de vida')

#ataques
selecao = input('Selecione o ataque [Fireball|Heal|Frozen] \n')

if classe == '1':
    if selecao == 'fireball':
        mhp = mhp - 6
        print (f'{m} recebeu 6 de dano [{mhp} hp]')
    elif selecao == 'heal':
        hp = hp + 10
        print(f'Seu hp é {hp}')
        if hp > 79:
            hp = 8
    elif selecao == 'frozen':
        mhp = mhp - 5
        print (f'{m} recebeu 5 de dano [{mhp} hp]')
        


