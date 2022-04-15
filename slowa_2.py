from collections import Counter


def wczytaj_dane(param: str) -> list[list[str]]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split() for linia in file]


def licz_slowa_z_A_na_koncu(dane: list[list[str]]) -> int:
    result = 0
    for linia in dane:
        for slowo in linia:
            if slowo[-1] == 'A':
                result += 1


    return result


def szukaj_wierszy_gdzie_pierwsze_2_drugim(dane: list[list[str]]) -> int:
    result = 0
    for linia in dane:
        if linia[0] in linia[1]:
            result += 1
    return result


def jest_anagramem(linia: list[str]) -> bool:
    return Counter(linia[0]) == Counter(linia[1])

def szukaj_anagramy(dane: list[list[str]]) -> list[list[str]]:
    result = []
    for linia in dane:
        if jest_anagramem(linia):
            result.append(linia)
    return result


if __name__ == '__main__':
    dane = wczytaj_dane(r'.\dane2018_2\Dane_PR2\Dane_PR\slowa.txt')
    ile_slow_konczy_sie_na_A = licz_slowa_z_A_na_koncu(dane)
    print(ile_slow_konczy_sie_na_A)
    ile_wierszy_zawiera_pierwsze_w_drugim = szukaj_wierszy_gdzie_pierwsze_2_drugim(dane)
    print(ile_wierszy_zawiera_pierwsze_w_drugim)
    ile_anagramow = szukaj_anagramy(dane)
    print(ile_anagramow)