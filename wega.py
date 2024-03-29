

def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def szukaj_przeslania(dane: list[str]) -> str:
    result = []
    for indeks, slowo in enumerate(dane, 1):
        if indeks % 40 == 0:
            result.append(slowo[9])
    return ''.join(result)


def szukaj_najwiecej_liter(dane: list[str]) -> list[str, int]:
    maks = 0
    for linia in dane:
        dlugosc = len(set(linia))
        if dlugosc > maks:
            maks = dlugosc
    for linia in dane:
        dlugosc = len(set(linia))
        if dlugosc == maks:
            return [linia, dlugosc]


def czy_oddalone_o_maks_10(linia: str) -> bool:
    for indeks, litera in enumerate(linia):
        if indeks < len(linia) - 1:
            if ord(litera) - ord(linia[indeks + 1]) > 10:
                return False
    return True


def szukaj_slow_z_literami_oddalonymi_o_maks_10(dane: list[str]) -> list[str]:
    result = []
    for linia in dane:
        if czy_oddalone_o_maks_10(linia):
            result.append(linia)
    return result


if __name__ == '__main__':
    dane = wczytaj_dane(r'.\dane2018maj\Dane_PR2\sygnaly.txt')
    print(dane)
    przeslanie = szukaj_przeslania(dane)
    print(przeslanie)
    slowo_z_najwieksza_iloscia_roznych_liter = szukaj_najwiecej_liter(dane)
    print(slowo_z_najwieksza_iloscia_roznych_liter)
    slowa_z_literami_oddalonymi_o_maks_10 = szukaj_slow_z_literami_oddalonymi_o_maks_10(dane)
    print(slowa_z_literami_oddalonymi_o_maks_10)

