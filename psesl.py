from collections import Counter


def wczytaj_dane(param: str) -> list:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def ile_w_grudniu(pesele: list) -> int:
    result = 0
    for pesel in pesele:
        miesiac = pesel[2:4]
        if miesiac == '12':
            result += 1
    return result


def ile_kobiet(pesele: list) -> int:
    result = 0
    for pesel in pesele:
        plec = pesel[-2]
        if plec in ['2', '4', '6', '8']:
            result += 1
    return result


def kiedy_najwiecej(pesele: list) -> str:
    result = {}
    for pesel in pesele:
        rok = pesel[0:2]
        if result.get(rok):
            result[rok] += 1
        else:
            result[rok] = 1

    counter = Counter(result)
    return '19' + counter.most_common()[0][0]


def jest_poprawny(pesel: str) -> bool:
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = 0
    for indeks, waga in enumerate(wagi):
        suma += waga * int(pesel[indeks])
    reszta = suma % 10
    if reszta == 0:
        cyfra_kontrolna = 0
    else:
        cyfra_kontrolna = 10 - reszta

    return cyfra_kontrolna == int(pesel[-1])


def bledny_pesel(pesele: list)   -> list:
    result = []
    for pesel in pesele:
        if not jest_poprawny(pesel):
            result.append(pesel)

    return sorted(result)


def zestawienie(pesele: list) -> dict:
    result = {}
    for pesel in pesele:
        rok = pesel[0]

        if not result.get(rok):
            result[rok] = 1
        else:
            result[rok] += 1
    return result


if __name__ == '__main__':
    dane = wczytaj_dane('./dane2010/pesel.txt')
    ile_w_grudniu(dane)
    ile_kobiet(dane)
    kiedy_najwiecej(dane)
    bledny_pesel(dane)
    zestawienie(dane)
