import math
import time
import os

def loop():
    print("Going back to home screen in 10 seconds")
    time.sleep(10)
    cls()
    main()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def calcularlsd(x = 0, n = 0):

    x = int(input("Lsd dosage in ug: "))
    n = int(input("Days since you've used lsd: "))

    if n < 0 or n > 12:
        print("Days need to be above 0 and below 12 (when the tolerance is gone)")
        loop()
    else:
        dosagem = (x / 100) * 280.059565 * (math.pow(n,-0.41256595))
        print("You will need to take {:.0f}ug to feel the same effects as {:.1f}ug".format(dosagem, x))
        loop()

def calcularcogu(x = 0, n = 0):

    x = int(input("Last dosage in grams: "))
    n = int(input("Days since you've used mushrooms: "))

    if n < 0 or n > 12:
        print("Days need to be above 0 and below 12 (when the tolerance is gone)")
        loop()
    else:
        dosagem = (x / 100) * 280.059565 * (math.pow(n,-0.41256595))
        print("You will need to take {:.0f}g to feel the same effects as {:.1f}g".format(dosagem, x))
        loop()


def calcularmdma(x = 0, y = 0):
    x = float(input("Type your weight in kg: "))
    y = x * 1.5
    print("Safe dosage: {:.0f}mg".format(y))
    loop()


def main():
    escolha = input("1 - Calculate lsd tolerance \n2 - Calculate mushroom tolerance\n3 - Calculate a safe dosage of MDMA")
    if escolha == '1':
        calcularlsd()
    elif escolha == '2':
        calcularcogu()
    elif escolha == '3':
        calcularmdma()
    else:
        print("Please type a correct option")
        time.sleep(3)
        main()

main()
