def wczytaj_dane(param: str) -> list[list[str]]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split() for linia in file]

def jest_pierwsza(liczba: int) -> bool:
    if liczba == 0 or liczba == 1:
        return False
    elif liczba == 2:
        return True
    elif liczba % 2 == 0:
        return False
    else:
        for i in range(3, liczba, 2):
            if liczba % i == 0:
                return False
    return True

def jest_parzysta(linia: list[str]) -> bool:
    return int(linia[0]) % 2 == 0


def rozbijaj(linia: list[str], pierwsze: list[int]) -> list[int]:
    result = []
    linia = int(linia[0])
    for pierwsza in pierwsze:
        if linia - pierwsza in pierwsze:
            return [linia, pierwsza]


def rozbij(dane: list[list[str]]) -> list[list[int]]:
    result = []
    for linia in dane:
        if jest_parzysta(linia) and int(linia[0]) > 4:
            result.append(rozbijaj(linia,pierwsze))

    return result


def zrob_pierwsze(param: int) -> list[int]:
    result = []
    for i in range(3, param, 2):
        if jest_pierwsza(i):
            result.append(i)
    return result
if __name__ == '__main__':
    dane = wczytaj_dane(r'.\dane_2020\Dane_PR2\pary.txt')
    print(dane)
    pierwsze = zrob_pierwsze(100)
    rozbite = rozbij(dane)
    # print(pierwsze)
    print(rozbite)
