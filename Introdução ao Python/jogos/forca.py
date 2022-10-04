def jogar():
    print('*****************************************')
    print('****** Bem-vindo ao jogo da Forca *******')
    print('*****************************************')

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = chute
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))

        if erros == 6:
            break
        elif "_" not in letras_acertadas:
            break

        print(letras_acertadas)
        print("Jogando...")



    if "_" not in letras_acertadas:
        print("VOCÊ VENCEU !!!")
    else:
        print("ENFORCADO !!! ")

    print("Fim do jogo")


if (__name__ == '__main__'):
    jogar()
