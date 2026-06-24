import random #random

start = input ("Start? [Y/N]\n")
if start == "y":
    print ("***************************************")
if start == "y":
    nome = input ("Defina um nick: ")
elif start == "n":
    print ("Ta aqui porque então? ")

print ("***************************************")

print (f"Muito bem {nome}, vamos começar o jogo...")

print ("***************************************")

m = 0 #magia
f = 0 #força
v = 0 #velocidade

classe = input ("Escolha uma classe entre Mago/Guerreiro ")
if classe == "mago":
    m = random.randint(5,7)
    f = random.randint(1,2)
    v = random.randint(2,4)
elif classe == "guerreiro":
    m = random.randint(1,2)
    f = random.randint(5,7)
    v = random.randint(3,5)

print ("***************************************")

print (f"Seus status são: Magia {m}/Força {f}/velocidade {v}")

print ("***************************************")

print ("Em Elaria, um reino onde magia e tecnologia coexistem,")
print ("um antigo cataclismo ameaça o equilíbrio do mundo. Fragmentos mágicos,")
print ("que protegem o reino, foram escondidos para evitar que caíssem em mãos")
print ("erradas. Agora, um culto sombrio procura reunir esses fragmentos para")
print ("dominar Elaria.")
