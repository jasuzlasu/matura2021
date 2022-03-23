def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def ile_liczb(dane: list[str]) -> int:
    result = 0
    for linia in dane:
        if linia[0] == linia[-1]:
            result += 1
    return result


def zamien_liczby(dane: list[str]) -> list[str]:
    result = []
    for linia in dane:
        result.append(str(int(linia, 8)))
    return result


def ktora_liczba_spelnia_warunek(dane: list[str]) -> list[str]:
    result = []
    for linia in dane:
        wszystkie_spelniaja_warunek = False
        for indeks, element in enumerate(linia):
            if indeks < len(element) - 1:

                if int(element) <= int(element[indeks + 1]):
                    wszystkie_spelniaja_warunek = True
                else:
                    wszystkie_spelniaja_warunek = False
                    break

        if wszystkie_spelniaja_warunek:
            result.append(int(linia))
    print(result)


if __name__ == '__main__':
    dane = wczytaj_dane('.\dane_2013\Dane_PR\dane.txt')
    ile_liczb(dane)
    zamienione_liczby = zamien_liczby(dane)
    ktora_liczba_spelnia_warunek(dane)
