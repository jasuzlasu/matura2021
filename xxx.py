def czytaj_dane_z_pliku(nazwa_pliku):
    with open(nazwa_pliku) as plik:
        dane = plik.readlines()

    return [linia.split() for linia in dane]


def tworz_neon(dane_z_pliku):
    neon = []
    for komenda, parametr in dane_z_pliku:
        if komenda == 'DOPISZ':
            neon.append(parametr)
        if komenda == 'USUN':
            neon.pop()
        if komenda == 'ZMIEN':
            neon.pop()
            neon.append(parametr)
        if komenda == 'PRZESUN':
            index = neon.index(parametr)
            neon.remove(parametr)
            if parametr != 'Z':
                neon.insert(index, chr(ord(parametr) + 1))
            else:
                neon.insert(index, 'A')
    return neon


def licz_instrukcje(dane_z_pliku):
    poprzednia_komenda = ''
    licznik_komend = {'DOPISZ': [], 'ZMIEN': [], 'USUN': [], 'PRZESUN': []}

    for komenda, parametr in dane_z_pliku:
        if komenda != poprzednia_komenda:
            licznik_komend[komenda].append(1)
        else:
            licznik_komend[komenda][-1] += 1
        poprzednia_komenda = komenda

    for klucz, wartosc in licznik_komend.items():
        licznik_komend[klucz] = max(wartosc)
    maks_klucz = ''
    maks = 0
    for klucz, wartosc in licznik_komend.items():
        if wartosc > maks:
            maks = wartosc
            maks_klucz = klucz

    print(maks_klucz, maks)


def licz_litery(dane_z_pliku):
    licznik_liter = {}
    for komenda, parametr in dane_z_pliku:
        if komenda == "DOPISZ":
            if not licznik_liter.get(parametr):
                licznik_liter[parametr] = 1
            else:
                licznik_liter[parametr] += 1
    maks = 0
    maks_klucz = 0
    for klucz, wartosc in licznik_liter.items():
        if wartosc > maks:
            maks = wartosc
            maks_klucz = klucz
    print(maks_klucz,maks)

if __name__ == '__main__':
    dane_z_pliku = czytaj_dane_z_pliku('instrukcje.txt')
    neon = tworz_neon(dane_z_pliku)


    # Odpowiedzi
    print('Zadanie 4.1')
    print(len(neon))

    print('Zadanie 4.2')
    licz_instrukcje(dane_z_pliku)

    print('Zadanie 4.3')
    licz_litery(dane_z_pliku)

    print('Zadanie 4.4')
    print(''.join(neon))

