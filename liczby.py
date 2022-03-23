import math


def wczytaj_dane(param: str) -> list[int]:
    with open(param) as file:
        file = file.readlines()
    return [int(linia.split()[0]) for linia in file]


def jest_potega_3(liczba: int, potegi: list[int]) -> bool:
    if liczba in potegi:
        return True
    else:
        return False


def szukaj_poteg_3(dane: list[int]) -> list[int]:
    result = []
    for liczba in dane:
        if jest_potega_3(liczba, potegi):
            result.append(liczba)

    return result


def tworz_potegi(n: int) -> list[int]:
    result = []
    i = 1
    while 3 ** i < n:
        result.append(3 ** i)
        i += 1
    return result


def jest_rowna_silni(liczba: int) -> bool:
    suma = 0
    liczba_lista = list(str(liczba))
    liczba_lista = [int(element) for element in liczba_lista]
    for i in liczba_lista:
        suma += math.factorial(i)
    return suma == liczba

def szukaj_liczb_rownych_silni(dane: list[int]) -> list[int]:
    result = []
    for liczba in dane:
        if jest_rowna_silni(liczba):
            result.append(liczba)
    return result


def nwd(param1: int, param2: int) -> int:
    mniejsza = min(param1, param2)
    for i in range(mniejsza, 2, -1):
        if param1 % i == 0 and param2 % i == 0:
            return i



if __name__ == '__main__':
    # dane = wczytaj_dane(r'.\maj2019\Dane_PR2\liczby.txt')
    # print(dane)
    # potegi = tworz_potegi(100_000)
    # print(potegi)
    # potegi_3 = szukaj_poteg_3(dane)
    # print(potegi_3)
    # liczby_rowne_silni = szukaj_liczb_rownych_silni(dane)
    # print(liczby_rowne_silni)
    print(nwd(28, 6))

