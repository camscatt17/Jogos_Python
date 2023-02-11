import Forca
import Adivinhacao

print("********************************")
print("Escolha seu jogo!")
print("*********************************")

print("(1) - Adivinhação")
print("(2) - Forca")

jogo = int(input("Qual o jogo escolhido? "))

if(jogo == 1):
    print("Jogar Adivinhação!")
    Adivinhacao.jogar()
else:
    print("Jogar Forca!")
    Forca.jogar()

