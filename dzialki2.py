TRAWA = '*'


def wczytaj_dane(param: str) -> list:
    with open(param) as file:
        file = file.readlines()
    dane = [dzialka.split() for dzialka in file]
    dzialki = []
    dzialka = []
    for linia in dane:
        if not linia == []:
            dzialka.append(linia[0])
        else:
            dzialki.append(dzialka)
            dzialka = []
    return dzialki


def pole_trawy(dzialka: list) -> int:
    pole = 0
    for linia in dzialka:
        pole += linia.count(TRAWA)
    return pole


def ile_dzialek_70(dzialki: list) -> int:
    result = 0
    for dzialka in dzialki:
        if pole_trawy(dzialka) > int((30*30)*0.7):
            result += 1
    return result


def odwroc_dzialki(dane: list) -> list:
    result = []
    for dzialka in dane:
        dzialka.reverse()
        result.append(dzialka)

    nowe_dzialki = []
    for indeks, dzialka in enumerate(result):
        nowa_linia = []
        for linia in dzialka:
            for litera in reversed(linia):
                nowa_linia.append(litera)
            nowa_linia = ''.join(nowa_linia)
            nowa_linia.append()

    return nowe_dzialki


if __name__ == "__main__":
    dane = wczytaj_dane('.\dane_2019\dzialki.txt')
    print(ile_dzialek_70(dane))
    odwrocone_dzialki =odwroc_dzialki(dane)
    print(odwrocone_dzialki)