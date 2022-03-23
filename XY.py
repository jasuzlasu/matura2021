def wczytaj_dane(param: str) -> list[list[int]]:
    with open(param) as file:
        file = file.readlines()
    file = [linia.split() for linia in file]
    file = [[int(linia[0]), int(linia[1])] for linia in file]
    return file


def jest_pierwsza(liczba: int) -> bool:
    if liczba == 2:
        return True
    result = False
    for i in range(3, liczba, 2):
        if liczba % i == 0:
            return False
        else:
            result = True
    return result


def szukaj_liczb_pierwszych(dane: list[list[int]]) -> list[list[int]]:
    result = []
    for x, y in dane:
        if jest_pierwsza(x) and jest_pierwsza(y):
            result.append([x, y])
    return result


def szykaj_liczb_cyfropodobnych(dane: list[list[int]]) -> list[list[int]]:
    result = []
    for x, y in dane:
        if set(str(x)) == set(str(y)):
            result.append([x, y])
    return result


def oblicz_odleglosc(punkt_1: list[int], punkt_2:list[int]) -> int:
    return int(((punkt_2[0] - punkt_1[0]) ** 2 + (punkt_2[1] - punkt_1[1]) ** 2) ** 0.5)


def szukej_najbardziej_oddalonych_punktow(dane: list[list[str]]) -> list[int]:
    indeks_1_max = None
    indeks_2_max = None
    max_odleglosc = 0
    for indeks_1, punkt_1 in enumerate(dane):
        for indeks_2, punkt_2 in enumerate(dane):
            odleglosc = oblicz_odleglosc(punkt_1, punkt_2)
            if odleglosc > max_odleglosc:
                max_odleglosc = odleglosc
                indeks_1_max = indeks_1
                indeks_2_max = indeks_2

    return [indeks_1_max, indeks_2_max]


def zapisz(param: str, wyniki: list[str]) ->None:
    with open(r'.\dane_2017a\MIN-DANE-2017\wyniki4.txt', 'w') as file:
        file.write('\n'.join(wyniki))


if __name__ == '__main__':
    wyniki = []
    dane = wczytaj_dane(r'.\dane_2017a\MIN-DANE-2017\punkty.txt')
    print(dane)
    liczby_pierwsze = szukaj_liczb_pierwszych(dane)
    print(liczby_pierwsze)
    liczby_cyfropodobne = szykaj_liczb_cyfropodobnych(dane)
    print(liczby_cyfropodobne)
    najbardziej_oddalone_punkty = szukej_najbardziej_oddalonych_punktow(dane)
    print(najbardziej_oddalone_punkty)
    punkt_A = dane[najbardziej_oddalone_punkty[0]]
    punkt_B = dane[najbardziej_oddalone_punkty[1]]
    odleglosc_A_B = oblicz_odleglosc(dane[najbardziej_oddalone_punkty[0]], dane[najbardziej_oddalone_punkty[1]])

    wyniki.append('zad4.1')
    wyniki.append(str(len(liczby_pierwsze)))
    wyniki.append('zad4.2')
    wyniki.append(str(len(liczby_cyfropodobne)))
    wyniki.append('zad4.3')
    wyniki.append(f'{punkt_A[0]} {punkt_A[1]} {punkt_B[0]} {punkt_B[1]} {odleglosc_A_B}')
    print(wyniki)
    zapisz(r'.\dane_2017a\MIN-DANE-2017\punkty.txt', wyniki)