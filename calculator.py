import math
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calcularlsd(x = 0, n = 0):

    x = int(input("Dose em ug: "))
    n = int(input("Dias desde o uso: "))

    dosagem = (x / 100) * 280.059565 * (math.pow(n,-0.41256595))
    print("Você vai precisar usar {:.1f}ug para sentir os mesmos efeitos de {:.1f}ug".format(dosagem, x))
    print("Voltando pra tela de inicio em 5 segundos")
    time.sleep(5)
    cls()
    main()

def calcularmdma(x = 0, y = 0):
    x = float(input("Digite seu peso: "))
    y = x * 1.5
    print("Dosagem segura: {:.0f}mg".format(y))
    print("Voltando pra tela de inicio em 5 segundos")
    time.sleep(5)
    cls()
    main()


def main():
    escolha = input("1 - Calcular tolerancia de psicodélicos \n2 - Calcular dosagem segura de MDMA\n")
    if escolha == '1':
        calcularlsd()
    elif escolha == '2':
        calcularmdma()



main()
