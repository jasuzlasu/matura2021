def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def jest_dwucykliczna(linia: str) -> bool:
    result = False
    polowa = int(len(linia) / 2)
    return linia[:polowa] == linia[polowa:]

def szukaj_dwucyklicznych(dane: list[str]) -> list[str]:
    result = []
    for linia in dane:
        if jest_dwucykliczna(linia):
            result.append(linia)
    return result


def szukaj_najwiekszego_dwucyklicznego(dwucykliczne: list[str]) -> str:
    result = ''
    max = 0
    for linia in dwucykliczne:
        if len(linia) > max:
            max = len(linia)
            result = linia
    return result


def jest_niepoprawna(linia: str) -> bool:
    for indeks in range(0, len(linia), 4):
        liczba_dziesietna = int(linia[indeks:indeks + 4], 2)
        if liczba_dziesietna > 9:
            return True
    return False

def szukaj_niepoprawnych(dane: list[str]) -> list[str]:
    result = []
    for linia in dane:
        if jest_niepoprawna(linia):
            result.append(linia)
    return result


def szukaj_najwiekszej(dane: list[str]) -> str:
    MAX = 65535
    mniejsze_od_65535 = [int(linia, 2) for linia in dane if int(linia, 2) <= MAX]

    return f'{max(mniejsze_od_65535)}, {bin(max(mniejsze_od_65535))[2:]}'


def zapisz(param: str, wyniki:list[str]) -> None:
    with open(param, 'w') as file:
        file.write('\n'.join(wyniki))


if __name__ == '__main__':
    dane = wczytaj_dane(r'.\dane_2017\Dane_PR2\binarne.txt')
    print(dane)
    dwucykliczne = szukaj_dwucyklicznych(dane)
    najw_dwucykliczny = szukaj_najwiekszego_dwucyklicznego(dwucykliczne)
    niepoprawne = szukaj_niepoprawnych(dane)
    najwieksza = szukaj_najwiekszej(dane)
    wyniki = ['zad1']
    wyniki.append(str(len(dwucykliczne)))
    wyniki.append('zad2')
    wyniki.append(str(len(niepoprawne)))
    wyniki.append('zad3')
    wyniki.append(najwieksza)
    print(wyniki)
    zapisz(r'.\dane_2017\Dane_PR2\zad4.txt',wyniki)