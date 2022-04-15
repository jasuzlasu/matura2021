from unicodedata import digit


def wczytaj_dane(param: str) -> list[int]:
    with open(param) as file:
        file = file.readlines()
    return [int(linia.split()[0]) for linia in file]


def jest_nieparzysta(liczba: int) -> bool:
    return liczba % 2 != 0


def szukaj_nieparzystych(dane: list[int]) -> int:
    result = 0
    for liczba in dane:
        if jest_nieparzysta(liczba):
            result += 1

    return result


def suma_cyfr(liczba: int) -> int:
    suma = 0
    while liczba > 0:
        suma += liczba % 10
        liczba /= 10
    return int(suma)


def szukaj_sumy_11(dane: list[int]) -> int:
    result = 0
    for liczba in dane:
        if suma_cyfr(liczba) == 11:
            result += 1
    return result


def jest_pierwsza(liczba: int) -> bool:
    if liczba == 0 or liczba == 1:
        return False
    elif liczba == 2:
        return True
    elif liczba % 2 == 0:
        return False
    else:
        for i in range(3, liczba, 2):
            if i % 2 == 0:
                return False
    return True


def szukaj_liczb_pierwszych_z_przedzialu(dane: list[int]) -> list[int]:
    result = []
    for liczba in dane:
        if 4000 <= liczba <= 5000:
            if jest_pierwsza(liczba):
                result.append(liczba)
    return result


if __name__ == '__main__':
    dane = wczytaj_dane(r'.\Dane_PP2s\liczby.txt')
    print(dane)
    nieparzyste = szukaj_nieparzystych(dane)
    print(nieparzyste)
    ile_liczb_z_suma_11 = szukaj_sumy_11(dane)
    print(ile_liczb_z_suma_11)
    liczby_pierwsze_z_przedzialu = szukaj_liczb_pierwszych_z_przedzialu(dane)
    print(liczby_pierwsze_z_przedzialu)
