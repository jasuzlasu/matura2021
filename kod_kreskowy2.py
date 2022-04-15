KODY_CYFR = {0: '10101110111010',
             1: '11101010101110',
             2: '10111010101110',
             3: '11101110101010',
             4: '10101110101110',
             5: '11101011101010',
             6: '10111011101010',
             7: '10101011101110',
             8: '11101010111010',
             9: '10111010111010'}
START = '11011010'
STOP = '11010110'


def wczytaj_dane_liczby(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    file = [linia.split()[0] for linia in file]
    return file


def sumuj_cyfry_na_pozycji_parzystej(liczba: str) -> str:
    liczba = liczba[::-1]
    return str(int(liczba[0]) + int(liczba[2]) + int(liczba[4]))


def sumuj_cyfry_na_pozycji_nieparzystej(liczba: str) -> str:
    liczba = liczba[::-1]
    return str(int(liczba[1]) + int(liczba[3]) + int(liczba[5]))


def dziel_liczby(liczby: list[str]) -> list[list[str]]:
    result = []

    for liczba in liczby:
        suma_parzyste = ''
        suma_nieparzyste = ''
        suma_parzyste += sumuj_cyfry_na_pozycji_parzystej(liczba)
        suma_nieparzyste += sumuj_cyfry_na_pozycji_nieparzystej(liczba)
        result.append([suma_parzyste, suma_nieparzyste])

    return result


def szukaj_cyfry_kontrolnej(liczby: list[str], podzielone_liczby: list[list[str]]) -> list[str]:
    result = []
    for liczba, sumy_cyfr in zip(liczby, podzielone_liczby):
        cyfra_kontrolna = 0
        suma_par = sumy_cyfr[0]
        suma_niepar = sumy_cyfr[1]
        cyfra_kontrolna = (int(suma_par) * 3) + int(suma_niepar)
        cyfra_kontrolna = cyfra_kontrolna % 10
        cyfra_kontrolna = 10 - cyfra_kontrolna
        cyfra_kontrolna = cyfra_kontrolna % 10
        result.append([liczba, str(cyfra_kontrolna)])
    return result


def tworz_kody_s25(cyfry_kontrolne: list[str], KODY_CYFR: dict[int: str]) -> list[str]:
    result = []
    for liczba, cyfra_kontrolna in cyfry_kontrolne:
        kod_s25 = ''
        kod_s25 = START + \
                  KODY_CYFR[int(liczba[0])] + \
                  KODY_CYFR[int(liczba[1])] + \
                  KODY_CYFR[int(liczba[2])] + \
                  KODY_CYFR[int(liczba[3])] + \
                  KODY_CYFR[int(liczba[4])] + \
                  KODY_CYFR[int(liczba[5])] + \
                  STOP
        result.append(kod_s25)
    return result


if __name__ == '__main__':
    liczby = wczytaj_dane_liczby(r'.\dane_2015\MIN-R2A1P-153_dane\kody.txt')
    podzielone_liczby = dziel_liczby(liczby)
    print(liczby)
    print(dziel_liczby(liczby))
    cyfry_kontrolne = szukaj_cyfry_kontrolnej(liczby, podzielone_liczby)
    print(tworz_kody_s25(cyfry_kontrolne, KODY_CYFR))
