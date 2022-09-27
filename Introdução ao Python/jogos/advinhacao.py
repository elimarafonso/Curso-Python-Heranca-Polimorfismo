print("*********************************")
print("Bem vindo a jogo de adivinhação !")
print("*********************************")

numero_secreto = 42

chute = input("Tente adivinhar o número: ")
print("Você digitou", chute )

chute_int = int(chute)

if (numero_secreto == chute_int):
    print("################")
    print("você acertou !!")
    print("################")
else:
    print("------------------")
    print("ERROOOUUU")
    print("------------------")

print("fim do jogo.")

