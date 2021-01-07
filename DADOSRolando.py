import random

print("OLá, Seja Bem Vindo ao teste")


def SELDADOS():
    return print(random.randint(1, 6))


def DADOS():
    termo = input("Jogar Dados? (y/n)")
    while termo == "y":
        print("Rolandinho!")
        SELDADOS()
        termo = input("Novamente? (y/n)")

    if termo == "n":
        print("Obrigado por jogar!")


DADOS()
