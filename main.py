neon = []
licznik_liter = {}


def dopisz():
    neon.append(parametr)

def usun():
    neon.pop()

def zmien():
    neon.pop()
    neon.append(parametr)

def przesun():
    index = neon.index(parametr)
    neon.remove(parametr)
    if parametr != 'Z':
        neon.insert(index, chr(ord(parametr) + 1))
    else:
        neon.insert(index, 'A')

def licz_wystapienia_liter():
    if licznik_liter.get(parametr):
        licznik_liter[parametr] += 1
    else:
        licznik_liter[parametr] = 1

def podaj_najczesciej_wystepujaca_litere():
    max_litera = ''
    max_ilosc = 0

    for litera, ilosc in licznik_liter.items():
        if ilosc > max_ilosc:
            max_litera = litera
            max_ilosc = ilosc
    return max_litera, max_ilosc


if __name__ == '__main__':

    with open('instrukcje.txt', 'r') as file:
        instrukcje = file.readlines()
    licznik_komend = {}
    licznik_komend_max = {}
    poprzednia_komenda = 0
    for instrukcja in instrukcje:
        komenda, parametr = instrukcja.split()

        if poprzednia_komenda == 0:
            licznik_komend[komenda] = 1
        elif poprzednia_komenda == komenda:
            licznik_komend[komenda] +=1
        else:
            licznik_komend_max = licznik_komend


        poprzednia_komenda = komenda


        if komenda == "DOPISZ":
            dopisz()
            licz_wystapienia_liter()
        elif komenda == "USUN":
            usun()
        elif komenda == "ZMIEN":
            zmien()
        elif komenda == "PRZESUN":
            przesun()
        poprzednia_komenda = komenda


    # wyniki ostateczne
    print('Zadanie 4.1')
    print(len(neon))
    print('Zadanie 4.4')
    print(''.join(neon))
    print('Zadanie 4.3')
    print(podaj_najczesciej_wystepujaca_litere())