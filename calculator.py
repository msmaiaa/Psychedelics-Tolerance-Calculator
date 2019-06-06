import math
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calcularlsd(x = 0, n = 0):

    x = int(input("Lsd dosage in ug: "))
    n = int(input("Days since you've used lsd: "))

    dosagem = (x / 100) * 280.059565 * (math.pow(n,-0.41256595))
    print("You will need to take {:.1f}ug to feel the same effects as {:.1f}ug".format(dosagem, x))
    print("Going back to home screen in 5 seconds")
    time.sleep(5)
    cls()
    main()

def calcularmdma(x = 0, y = 0):
    x = float(input("Type your weight in kg: "))
    y = x * 1.5
    print("Safe dosage: {:.0f}mg".format(y))
    print("Going back to home screen in 5 seconds")
    time.sleep(5)
    cls()
    main()


def main():
    escolha = input("1 - Calculate lsd tolerance \n2 - Calculate a safe dosage of MDMA\n")
    if escolha == '1':
        calcularlsd()
    elif escolha == '2':
        calcularmdma()



main()
