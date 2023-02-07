import random
print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("*********************************")

print("Qual nível de dificuldade?")
print("(1)Fácil")
print("(2)Médio")
print("(3)Difícil")

#Inicialização das variáveis
nivel = int(input("Define o nível: "))
numero_secreto = 0
intervalo = 0

#Determinação da dificuldade do jogo
if(nivel == 1):
    total_tentativas = 10
    numero_secreto = int(random.randrange(1, 51))
    intervalo = 50

elif(nivel == 2):
    total_tentativas = 5
    numero_secreto = int(random.randrange(1, 101))
    intervalo = 100

elif(nivel == 3):
    total_tentativas = 3
    numero_secreto = int(random.randrange(1, 151))
    intervalo = 150

else:
    total_tentativas = 10
    numero_secreto = int(random.randrange(1, 51))
    intervalo = 50

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = input("Digite o seu número entre 1 e {}: ".format(intervalo))

    print("Você digitou: ", chute)
    chute = int(chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print('Você acertou!')
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu número é menor que o número secreto.")


print("Fim de jogo!")
