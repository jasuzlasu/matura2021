import math

POTEGI_3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]

def wczytaj_dane(param: str) -> list[int]:
    with open(param) as file:
        file = file.readlines()
    return [int(linia.split()[0]) for linia in file]


def jest_potega_3(liczba: int) -> bool:
    return liczba in POTEGI_3


def szukaj_poteg(dane: list[int]) -> int:
    result = 0
    for liczba in dane:
        if jest_potega_3(liczba):
            result += 1
    return result


def rozbij_liczbe(liczba: int) -> list[int]:
    return [int(cyfra) for cyfra in str(liczba)]


def szukaj_liczb_rownych_silni(dane: list[int]) -> list[int]:
    result = []
    for liczba in dane:
        rozbita_liczba = rozbij_liczbe(liczba)
        suma_cyfr = 0
        for cyfra in rozbita_liczba:
            suma_cyfr += math.factorial(cyfra)
        if suma_cyfr == liczba:
            result.append(liczba)
    return result







def tworz_dzielniki(dane: list[int]) -> list[list[int]]:
    result = []
    dzielniki_liczby = []
    for liczba in dane:
        dzielniki_liczby =[]
        for i in range(1, liczba + 1):
            if liczba % i == 0:
                dzielniki_liczby.append(i)
        result.append(dzielniki_liczby)
    return result


def szukaj_ciagu_NWD(dane: list[int], lista_dzielnikow: list[list[int]]) -> list[int]:
    for indeks1, dzielniki1 in enumerate(lista_dzielnikow):
        for indeks2, dzielniki2 in enumerate(lista_dzielnikow):



if __name__ == '__main__':
    dane = wczytaj_dane(r'.\maj2019\Dane_PR2\liczby.txt')
    potegi_3 = szukaj_poteg(dane)
    print(dane)
    print(potegi_3)
    liczby_rowne_swojej_silni = szukaj_liczb_rownych_silni(dane)
    print(liczby_rowne_swojej_silni)
    dzielniki = tworz_dzielniki(dane)
    najdl_ciag_liczb_NWD = szukaj_ciagu_NWD(dane, dzielniki)
