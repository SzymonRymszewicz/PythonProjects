from Game import Game


def absolute():
    a = float(input("Podaj zmienna: "))
    if a >= 0:
        print("Twoja zmienna(bez zmain):", a)
    else:
        print("Twoja zmienna(bezwzgledna): ", a * -1)


def sgn():
    a = float(input("Podaj zmienna: "))
    if a > 0:
        print("znak: +")
    elif a < 0:
        print("znak: -")
    else:
        print("znak: 0")


def divide():
    a = float(input("Podaj zmienna 1: "))
    b = float(input("Podaj zmienna 2: "))

    if b != 0:
        print(a, " / ", b, " = ", a / b)
    else:
        print("Nie poprawna wartosc")


if __name__ == '__main__':
    Game()
