def wczytaj_dane(param: str) -> list:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def ile_w_grudniu(dane: list) -> int:
    result = 0
    for pesel in dane:
        if pesel[2:4] == '12':
            result += 1
    return result


def ile_kobiet(dane: list) -> int:
    result = 0
    for pesel in dane:
        if pesel[-2] in ['2', '4', '6', '8']:
            result += 1
    return result


def kiedy_najwiecej(dane: list) -> str:
    lata = {}
    for pesel in dane:
        if lata.get(pesel[:2]):
            lata[pesel[:2]] += 1
        else:
            lata[pesel[:2]] = 1
    from collections import Counter
    counter = Counter(lata)
    return '19' + counter.most_common()[0][0]


def jesli_pesel_jest_prawidlowy(pesel: str) -> bool:
    suma = 0
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    for indeks, waga in enumerate(wagi):
        suma += waga * int(pesel[indeks])
    reszta = suma % 10
    if reszta == 0:
        cyfra_kontrolna = 0
    else:
        cyfra_kontrolna = 10 - reszta
    return int(pesel[-1]) == cyfra_kontrolna

def bledne_pesele(dane: list) -> list:
    result = []
    for pesel in dane:
        if not jesli_pesel_jest_prawidlowy(pesel):
            result.append(pesel)
    return sorted(result)


def zestawienie(dane: list) -> dict:
    result = {}
    for pesel in dane:
        rok = pesel[0]
        if result.get(rok):
            result[rok] += 1
        else:
            result[rok] = 1
    return result




if __name__ == '__main__':
    dane = wczytaj_dane('.\dane2010\pesel.txt')
    ile_w_grudniu(dane)
    ile_kobiet(dane)
    kiedy_najwiecej(dane)
    bledne_pesele(dane)
    print(zestawienie(dane))

