
def dopisz(parametr):
    neon.append(parametr)


def zmien(parametr):
    neon.pop()
    neon.append(parametr)


def usun():
    neon.pop()


def przesun():
    index = neon.index(parametr)
    neon.pop(index)
    if parametr == 'Z':
        neon.insert(index, 'A')
    else:
        neon.insert(index, chr(ord(parametr) + 1))


def licz_litery():
    if licznik_liter.get(parametr):
        licznik_liter[parametr] += 1
    else:
        licznik_liter[parametr] = 1


def podaj_max():
    litera = ''
    max_wartosc = 0
    for klucz, wartosc in licznik_liter.items():
        if wartosc > max_wartosc:
            max_wartosc = wartosc
            litera = klucz
    return litera, max_wartosc


def najdluzszy_ciag_instrukcji(komenda):
    poprzednia_komenda = ''
    if komenda != poprzednia_komenda:
        if not licznik_instrukcji.get(komenda):
            licznik_instrukcji[komenda] = [1]
    else:
        licznik_instrukcji[komenda][-1] += 1


if __name__ == '__main__':
    neon = []
    licznik_liter = {}
    licznik_instrukcji = {}
    with open('instrukcje.txt') as file:
        instrukcje = file.readlines()

    for instrukcja in instrukcje:
        komenda, parametr = instrukcja.split()
        if komenda == 'DOPISZ':
            dopisz(parametr)
            licz_litery()
        elif komenda == 'ZMIEN':
            zmien(parametr)
        elif komenda == 'USUN':
            usun()
        elif komenda == 'PRZESUN':
            przesun()
        najdluzszy_ciag_instrukcji(komenda)

    litera, max_wartosc = podaj_max()

    print(len(neon))
    print(''.join(neon))
    print(litera, max_wartosc)
    print(licznik_instrukcji)