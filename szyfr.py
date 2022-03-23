nr_litery = {}
for i in range(65, 91):
    nr_litery[chr(i)] = i - 64


def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split()[0] for linia in file]


def rozszerz_klucz(klucz: str, param: int) -> str:
    result = list(klucz)
    while param > len(result):
        result += list(klucz)
    return ''.join(result)


def szyfruj_slowo(slowo: str, klucz: str) -> str:
    result = []

    if len(slowo) > len(klucz):
        klucz = rozszerz_klucz(klucz, len(slowo))

    for indeks, litera in enumerate(slowo):
        wynik = ord(litera) + nr_litery[klucz[indeks]]
        if wynik > 90:
            wynik -= 26
        result.append(chr(wynik))

    return ''.join(result)


def szyfruj(dane_niezaszyfrowane: list[str], dane_klucze_1: list[str]) -> list[str]:
    result = []
    for slowo, klucz in zip(dane_niezaszyfrowane, dane_klucze_1):
        result.append(szyfruj_slowo(slowo, klucz))

    return result


def odszyfruj_slowo(slowo: str, klucz: str) -> str:
    result = []

    if len(slowo) > len(klucz):
        klucz = rozszerz_klucz(klucz, len(slowo))
    for indeks, litera in enumerate(slowo):
        wynik = ord(litera) + nr_litery[klucz[indeks]]
        if wynik < 65:
            wynik += 26
        if wynik > 90:
            wynik -= 26
        result.append(chr(wynik))
    return ''.join(result)


def deszyfruj(dane_zaszyfrowane: list[str], dane_klucze_2: list[str]) -> list[str]:
    result = []
    for slowo, klucz in zip(dane_zaszyfrowane, dane_klucze_2):
        result.append(odszyfruj_slowo(slowo, klucz))

    return result


def zapisz_zaszyfrowane(zaszyfrowane: list[str], sciezka: str) -> None:
    with open(sciezka,'w') as file:
        file.write('\n'.join(zaszyfrowane))



if __name__ == '__main__':
    dane_niezaszyfrowane = wczytaj_dane(r'.\dane_2012\Dane_PR\tj.txt')
    dane_zaszyfrowane = wczytaj_dane(r'.\dane_2012\Dane_PR\sz.txt')

    dane_klucze_1 = wczytaj_dane(r'.\dane_2012\Dane_PR\klucze1.txt')
    dane_klucze_2 = wczytaj_dane(r'.\dane_2012\Dane_PR\klucze2.txt')

    zaszyfrowane = szyfruj(dane_niezaszyfrowane, dane_klucze_1)
    odszyfrowane = deszyfruj(zaszyfrowane, dane_klucze_1)

    zapisz_zaszyfrowane(zaszyfrowane, r'.\dane_2012\Dane_PR\wynik4a.txt')
    zapisz_zaszyfrowane(odszyfrowane, r'.\dane_2012\Dane_PR\wynik4b.txt')