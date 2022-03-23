def wczytaj_dane(param: str) -> list[list[int]]:
    with open(param) as file:
        file = file.readlines()
    return [[int(linia.split()[0]), int(linia.split()[1])] for linia in file]


def jest_pierwsza(x: int) -> bool:
    if x == 0 or x == 1 or x % 2 == 0:
        return False
    elif x == 2:
        return True
    else:
        for i in range(3,x,2):
            if x % i == 0:
                return False
    return True




def szukaj_liczb_pierwszych(dane: list[list[int]]) -> list[list[int]]:
    result = []
    for x , y in dane:
        if jest_pierwsza(x) and jest_pierwsza(y):
            result.append([x,y])
    return result


def sa_cyfropodobne(x: int, y: int) -> bool:
    return set(str(x)) == set(str(y))


def szukaj_cyfropodobnych(dane:list[list[int]]) -> list[list[int]]:
    result = []
    for x, y in dane:
        if sa_cyfropodobne(x, y):
            result.append([x, y])
    return result


def szukaj_najbardziej_oddalonych(dane:list[list[int]]) -> list[list[int]]:
    max_odleglosc = 0
    p1_max = None
    p2_max = None
    for x1, y1 in dane:
        for x2, y2 in dane:
            odleglosc = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            if odleglosc > max_odleglosc:
                max_odleglosc = odleglosc
                p1_max = [x1, y1]
                p2_max = [x2, y2]
    return [p1_max, p2_max, int(max_odleglosc)]


def szukaj_wewnatrz_kwadratu(dane: list[list[int]]) -> list[int]:
    wewnatrz = 0
    na_bokach = 0
    na_zewnatrz = 0
    for x, y in dane:
        if x < 5000 and y < 5000:
            wewnatrz += 1
        elif x == 5000 or y == 5000:
            na_bokach += 1
        else:
            na_zewnatrz += 1
    return [wewnatrz, na_bokach, na_zewnatrz]


if __name__ == '__main__':
    dane = wczytaj_dane(r'.\dane_2017a\MIN-DANE-2017\punkty.txt')
    print(dane)
    print(len(szukaj_liczb_pierwszych(dane)))
    print(szukaj_cyfropodobnych(dane))
    print(szukaj_najbardziej_oddalonych(dane))
    print(szukaj_wewnatrz_kwadratu(dane))