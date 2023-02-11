import random
def print_mensagem_abertura():
    print("********************************")
    print("Bem vindo ao jogo de Forca")
    print("*********************************")

def jogar():

    print_mensagem_abertura()

    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    palavra_secreta = palavras[random.randrange(0, len(palavras))]
    print("a palavra secreta é :", palavra_secreta)
    print("\nA palavra secreta tem {} letras:".format(len(palavra_secreta)))
    letras_acertadas = ["_" for letra in palavra_secreta]

    print(letras_acertadas)

    letras_faltando = int(letras_acertadas.count('_'))
    print('Ainda faltam acertar {} letras'.format(letras_faltando))

    enforcou = False
    acertou = False
    erros = 0
    tentativas = len(palavra_secreta)

    while(not enforcou and not acertou):
        chute = input("\nQual o seu chute? ").strip()
        tentativas -= 1
        if(chute.upper() in palavra_secreta.upper()):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                    print("Você acertou e ainda tem {} tentativas\n".format(tentativas))
                index += 1

        else:
            erros += 1
            print("Vocâ errou e ainda tem {} tentativas!\n".format(tentativas))

        letras_faltando = int(letras_acertadas.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))

        enforcou = tentativas == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Parabéns, você acertou a palavra secreta!")
    else:
        print("Que pena, você perdeu!")
    print("Fim de jogo!")

if(__name__=="__main__"):
    jogar()