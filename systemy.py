def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def ile_w_osemkowym(dane: list[str]) -> str:
    return [linia for linia in dane if linia[-1] == '8']


def czy_nie_ma_0(linia: str) -> bool:
    result = False
    for element in linia:
        if element == 0:
            return False
        else:
            result = True
    return result

def ile_w_czworkowym_bez_0(dane: list[str]) -> int:
    result = 0
    for linia in dane:
        if int(linia[-1]) == 4 and linia[:-1].count('0') == 0:
            result += 1

    return result


def ile_parzystych_dwojkowych(dane: list[str]) -> int:
    result = 0
    for linia in dane:
        if int(linia, 2) % 2 == 0:
            result += 1
    return result

    return result


if __name__ == '__main__':
    dane = wczytaj_dane(r'.\dane_2016\MIN-R2A1P-163_dane\liczby.txt')
    ile_liczb_w_osemkowym = len(ile_w_osemkowym(dane))
    print(dane)
    print(ile_liczb_w_osemkowym)
    # wyniki = []
    print(ile_w_czworkowym_bez_0(dane))
    # ile_parzystych_dwojkowych(dane)
