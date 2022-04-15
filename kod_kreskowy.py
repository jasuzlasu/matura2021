START = '11011010'
STOP = '11010110'

def wczytaj_dane(param: str) -> dict[int, str]:
    with open(param) as file:
        file = file.readlines()
    file = [linia.split() for linia in file]
    file.pop(0)
    return {int(linia[0]): linia[1] for linia in file}


def wczytaj_dane_kody(param: str) -> list[int]:
    with open(param) as file:
        file = file.readlines()
    file = [linia.split()[0] for linia in file]
    return file


def dziel_liczby(kody: list[int]) -> list[int]:
    result = []
    suma_parzyste = 0
    suma_nieparzyste = 0
    for liczba in kody:
        liczba = liczba[::-1]
        suma_parzyste += int(liczba[0]) + int(liczba[2]) + int(liczba[4])
        suma_nieparzyste += int(liczba[1]) + int(liczba[3]) + int(liczba[5])
        result.append([suma_parzyste, suma_nieparzyste])
        suma_parzyste = 0
        suma_nieparzyste = 0
    return result


def stworz_cyfre_konrolna_i_kod(kody: list[str], sumy: list[int], cyfry_kod):
    result = []
    for liczba, sumy_liczb in zip(kody, sumy):
        suma_kontrolna = sumy_liczb[0] * 3
        suma_kontrolna = suma_kontrolna + sumy_liczb[1]
        reszta = suma_kontrolna % 10
        cyfra_kontrolna = int(reszta % 10)
        kod = START +\
              cyfry_kod[liczba[0]] +\
              cyfry_kod[liczba[1]] +\
              cyfry_kod[liczba[2]] +\
              cyfry_kod[liczba[3]] +\
              cyfry_kod[liczba[4]] +\
              cyfry_kod[liczba[5]] +\
              cyfry_kod[liczba[cyfra_kontrolna]] + STOP
        result.append([cyfra_kontrolna, kod])

if __name__ == '__main__':
    kody = wczytaj_dane_kody(r'.\dane_2015\MIN-R2A1P-153_dane\kody.txt')
    cyfry_kod = wczytaj_dane(r'.\dane_2015\MIN-R2A1P-153_dane\cyfra_kodkreskowy.txt')
    print(kody)
    print(cyfry_kod)
    sumy = dziel_liczby(kody)
    print(sumy)
    cyfry_kontrolne_i_kody = stworz_cyfre_konrolna_i_kod(kody, sumy, cyfry_kod)