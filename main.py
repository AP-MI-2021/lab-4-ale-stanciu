def printMenu():
    print("1. Citirea unei liste care contine n numere intregi")
    print(
        "2. Afișați dacă un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție citită de la tastatură.")
    print("3. Afișați suma tuturor numerelor întregi pare din lista")
    print(
        "4. Afișați toate numere din lista care sunt pare. Daca se repeta un numar, acesta va apărea în lista rezultat doar o singura data.")


def citire_lista():
    l = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        l.append(int(input("L[" + str(i) + "]=")))
    return l


def gasire_numar(lst, numar, pozitia):
    """
    Afiseaza daca un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție citită de la tastatură
    :param lst: lista de nr. intregi
    :param n:
    :return: True, daca un număr citit de la tastatura se regaseste in lista începând de la o anumită poziție citită de la tastatură, False in caz contrar
    """
    # for i in range(pozitia, len(lst),1):
    # if

    for x in lst:
        index = lst.index(x)
        if index >= pozitia and x == numar:
            return True
    return False


def test_gasire_numar():
    assert gasire_numar([2, 32, 122, 12, 1456], 12, 3) == True
    assert gasire_numar([2, 32, 122, 12, 1456], 12, 4) == False


def suma_parelor(lst):
    """
    Afiseaza suma tuturor numerelor intregi pare din lista
    :param lst: lista de intregi
    :return:suma tuturor numerelor intregi pare din lista
    """
    rezultat = []
    for x in lst:
        if x % 2 == 0:
            rezultat.append(x)
    Sum = sum(rezultat)
    return Sum


def test_suma_parelor():
    assert suma_parelor([2, 3, 12, 5, 9]) == 14
    assert suma_parelor([13, 55, 31]) == 0


def afisare_pare(lst):
    """
    Afiseaza toate elementele pare din lista, o singura data
    :param lst: lista de numere intregi
    :return: o lista care contine toate elementele pare din lista, o singura data
    """
    rezultat = []
    y = 1
    for x in lst:
        if x % 2 == 0:
            rezultat.append(x)
    rezultat.sort()
    for x in rezultat:
        if y == x:
            rezultat.remove(x)
        y = x
    return rezultat



def test_afisare_pare():
    assert afisare_pare([23, 12, 3, 52, 12]) == [12, 52]
    assert afisare_pare([23, 51, 35]) == []


def main():
    test_gasire_numar()
    test_suma_parelor()
    test_afisare_pare()
    lst = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lst = citire_lista()
        elif optiune == "2":
            numar = int(input("Dati un numar: "))
            pozitia = int(input("Dati o pozitie: "))
            if gasire_numar(lst, numar, pozitia):
                print("DA")
            else:
                print("NU")
        elif optiune == "3":
            print(suma_parelor(lst))
        elif optiune == "4":
            print(afisare_pare(lst))


if __name__ == '__main__':
    main()
