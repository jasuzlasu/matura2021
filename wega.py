def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def znajdz_przeslanie(dane: list[str]) -> str:
    result = []
    for indeks, linia in enumerate(dane, 1):
        if indeks % 40 == 0:
            result.append(linia[9])
    return ''.join(result)


def znajdz_najwiecej_liter(dane: list[str]) -> list[str, int]:
    maks = 0
    for linia in dane:
        dlugosc = len(set(linia))
        if dlugosc > maks:
            maks = dlugosc
    for linia in dane:
        dlugosc = len(set(linia))
        if dlugosc == maks:
            return [linia, dlugosc]


def czy_odlegle_mniej_niz_10(linia: str) -> bool:
    for indeks, litera in enumerate(linia):
        if indeks < len(linia) - 1:
            if ord(litera) - ord(linia[indeks + 1]) > 10:
                return False
    return True

def szukaj_odleglych_mniej_niz_10(dane: list[str]) -> list[str]:
    result = []
    for linia in dane:
        if czy_odlegle_mniej_niz_10(linia):
            result.append(linia)
    return result


if __name__ == '__main__':

    dane = wczytaj_dane(r'.\dane2018maj\Dane_PR2\sygnaly.txt')
    print(dane)
    przeslanie = znajdz_przeslanie(dane)
    print(przeslanie)
    najw_liter = znajdz_najwiecej_liter(dane)
    print(najw_liter)
    odlegle = '\n'.join(szukaj_odleglych_mniej_niz_10(dane))
    print(odlegle)


