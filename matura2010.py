def wczytaj_dane_z_pliku(nazwa_pliku):
    result = []
    with open(nazwa_pliku) as file:
        result = file.readlines()

    return [linia. for linia in result]


def licz_litery(dane):
    liczba_liter = []

    for linia in dane:
        nowa_linia = []
        for slowo in linia:
            nowa_linia.append(len(slowo))
        liczba_liter.append(set(nowa_linia))
    odpowiedz = ''
    for indeks, linia in enumerate(liczba_liter):
        if len(linia) == 1:
            odpowiedz += " ".join(dane[indeks])
            odpowiedz += '\n'
    with open('odp4a.txt', 'w') as file:
        file.write(odpowiedz)


def is_anagram(pierwsze_slowo, slowo):
    return len(pierwsze_slowo) == len(slowo) and set(pierwsze_slowo) == set(slowo)


def znajdz_anagramy(dane):
    czy_byly_same_anagramy = True
    for linia in dane:
        pierwsze_slowo = linia[0]
        reszta_slow = linia[1:]
        for slowo in reszta_slow:
            if is_anagram(pierwsze_slowo, slowo):
                czy_byly_same_anagramy = True
            else:
                czy_byly_same_anagramy = False
                break
        if czy_byly_same_anagramy:
             print(linia)


def main():
    dane = (wczytaj_dane_z_pliku("./dane2010/anagram.txt"))
    print(dane)
    licz_litery(dane)
    znajdz_anagramy(dane)
if __name__ == "__main__":
    main()
