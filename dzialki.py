def wczytaj_dane(nazwa_pliku):
    with open(nazwa_pliku) as file:
        dane = file.readlines()
    dzialki = {}
    dzialka = []
    licznik_dzialek = 1
    for linia in dane:
        if linia != '\n':
            dzialka.append(linia.split()[0])
        else:
            dzialki[licznik_dzialek] = dzialka
            dzialka = []
            licznik_dzialek += 1
    return dzialki


def policz_70(dane_z_pliku):
    _70_PROCENT = int((30 * 30) * 0.7)
    licznik_trawy = 0

    for licznik_dzialek, dzialka in dane_z_pliku.items():
        for linia in dzialka:
            licznik_trawy += linia.count("*")
        if licznik_trawy > _70_PROCENT:
            print(licznik_dzialek, licznik_trawy)
        licznik_trawy = 0


def odwroc_dzialki(dane_z_pliku):
    odwrocone_dzialki = {}
    nie_odwrocona_lista = []
    for licznik_dzialek,dzialki in dane_z_pliku.items():
        for dzialka in dzialki:
            nie_odwrocona_lista.append(dzialka[::-1])
        odwrocone_dzialki[licznik_dzialek] = nie_odwrocona_lista[::-1]
        nie_odwrocona_lista = []


    for licznik_dzialek_z_pliku, dzialki_z_pliku in dane_z_pliku.items():
        for licznik_dzialek_odwroconych, dzialki_odwrocone in odwrocone_dzialki.items():
            if dzialki_z_pliku == dzialki_odwrocone:
                print(licznik_dzialek_z_pliku, licznik_dzialek_odwroconych)





def main():
    dane_z_pliku = wczytaj_dane(r'.\dane_2019\przyklad.txt')
    # policz_70(dane_z_pliku)
    odwroc_dzialki(dane_z_pliku)

if __name__ == '__main__':
    main()