from typing import Dict, List


def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def jest_dwucykliczny(linia: str) -> bool:
    polowa = int(len(linia) / 2)
    return linia[:polowa] == linia[polowa:]


def ile_dwucyklicznych(dane: list[str]) -> list[str]:
    result = []
    for linia in dane:
        if jest_dwucykliczny(linia):
            result.append(linia)
    return result


def szukaj_najwiekszej_dwucyklicznej(dwucykliczne: list[str]) -> str:
    result = ''
    max_dlugosc = 0
    for linia in dwucykliczne:
        if len(linia) > max_dlugosc:
            max_dlugosc = len(linia)
            result = linia
    return result


def dziel_na_4(dane: list[str]) -> list[list[int]]:
    result = []
    for linia in dane:
        podzielone = []
        for czworka in range(0, len(linia), 4):
            podzielone.append(int(linia[czworka:czworka + 4], 2))
        result.append(podzielone)

    print(result)
    return result


def czy_poprawny(element: int) -> bool:
    return element <= 9


def szukaj_niepoprawnnych(podzielone: list[list[int]]) -> dict[int, list[int]]:
    result = {}
    for indeks, linia in enumerate(podzielone):
        for element in linia:
            if not czy_poprawny(element):
                result[indeks] = linia
                break
    print(result)
    return result


def szukaj_najkrotszy(dane: list[str], indeksy: list[int]) -> int:
    minimum = 100000000000000
    for indeks in indeksy:
        if len(dane[indeks]) < minimum:
            minimum = len(dane[indeks])
    return minimum


def zapisz(param: str, wyniki: list[str]) -> None:
    print(wyniki)
    with open(param, 'w') as file:
        file.write('\n'.join(wyniki))


if __name__ == '__main__':
    dane = wczytaj_dane(r'.\dane_2017\Dane_PR2\binarne.txt')
    print(dane)
    dwucykliczne = ile_dwucyklicznych(dane)
    najwieksza_dwucykiczna = szukaj_najwiekszej_dwucyklicznej(dwucykliczne)

    podzielone = dziel_na_4(dane)
    niepoprawne = szukaj_niepoprawnnych(podzielone)
    najkrotszy_niepoprawny = szukaj_najkrotszy(dane, list(niepoprawne.keys()))

    wyniki = []
    wyniki.append('zad4.1')
    wyniki.append(str(len(dwucykliczne)))
    wyniki.append(najwieksza_dwucykiczna)
    wyniki.append(str(len(najwieksza_dwucykiczna)))
    wyniki.append('zad4.2')
    wyniki.append(str(len(niepoprawne)))
    wyniki.append(str(najkrotszy_niepoprawny))

    zapisz(r'.\dane_2017\Dane_PR2\zadanie4.txt', wyniki)
