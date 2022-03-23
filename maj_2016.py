def wczytaj_dane_1(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def wczytaj_dane_2(param: str) -> list[list[str]]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split() for linia in file]


def zaszyfruj_slowo(slowo: str, klucz: int) -> str:
    result = []
    for litera in slowo:
        kod_litery = ord(litera) + klucz
        if 65 <= kod_litery <= 90:
            x = chr(kod_litery)
        else:
            while kod_litery > 90:
                kod_litery -= 26
                x = chr(kod_litery)
        result.append(x)

    return ''.join(result)


def szyfruj(dane: list[str]) -> list[str]:
    result = []
    for slowo in dane:
        result.append(zaszyfruj_slowo(slowo, 1))
    return result


def odszyfruj_slowo(slowo: str, klucz: int) -> str:
    result = []
    for litera in slowo:
        kod_litery = ord(litera) - klucz
        if 65 <= kod_litery <= 90:
            pass
        else:
            while kod_litery < 65:
                kod_litery += 26
        result.append(chr(kod_litery))

    return ''.join(result)


def odszyfruj(dane: list[list[str]]) -> list[str]:
    result = []
    for slowo, klucz in dane:
        klucz = int(klucz)
        result.append(odszyfruj_slowo(slowo, klucz))
    return result


def blednie_zaszyfrowane(dane_3: list[list[str]]) -> list[str]:
    result = []
    czy_zaszyfrowany = False
    for slowo, szyfrogram in dane_3:
        for klucz in range(1, 9999 + 1):
            zaszyfrowane = zaszyfruj_slowo(slowo, klucz)
            if zaszyfrowane == szyfrogram:
                print(klucz)
                break
            else:
                czy_zaszyfrowany = False

        if czy_zaszyfrowany:
            result.append(slowo)

    return result


if __name__ == '__main__':
    dane_1 = wczytaj_dane_1(r'.\Dane_PR2\dane_6_1.txt')
    dane_2 = wczytaj_dane_2(r'.\Dane_PR2\dane_6_2.txt')
    dane_3 = wczytaj_dane_2(r'.\Dane_PR2\dane_6_3.txt')

    # print(dane_1)
    # print(dane_2)
    # zaszyfrowane = szyfruj(dane_1)
    # odszyfrowane = odszyfruj(dane_2)
    # print(blednie_zaszyfrowane(dane_3))
    print(blednie_zaszyfrowane([['AAA', 'BBB'], ['AAA', 'BBC']]))
