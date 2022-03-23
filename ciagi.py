def wczytaj_dane(param: str) -> list[str]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split() for linia in file]


def policz_takie_same_ostatnie(dane_1: list[list[str]], dane_2: list[list[str]]) -> int:
    result = 0
    for linia1, linia2 in zip(dane_1, dane_2):
        if linia1[-1] == linia2[-1]:
            result += 1
    return result


def ile_parzystych(linia1: list[str]) -> int:
    result = 0
    for element in linia1:
        if int(element) % 2 == 0:
            result += 1
    return result


def ile_nieparzystych(linia1: list[str]) -> int:
    result = 0
    for element in linia1:
        if not int(element) % 2 == 0:
            result += 1

    return result


def policz_ilosc_ciagow_z_parzystymi_i_nieparzystymi(dane_1: list[list[str]], dane_2: list[list[str]]) -> int:
    result = 0
    for linia1, linia2 in zip(dane_1, dane_2):
        if ile_parzystych(linia1) == 5 and ile_parzystych(linia2) == 5 and ile_nieparzystych(linia1) == 5 and ile_nieparzystych(linia2) == 5:
            result += 1
    return result


def policz_ilosc_ciagow_z_tych_samych_liczb(dane_1: list[list[str]], dane_2:[list[list[str]]]) -> int:
    result = []
    for indeks1, linia1 in enumerate(dane_1):
        for indeks2, linia2 in enumerate(dane_2):
            if set(linia1) == set(linia2):
                result.append([indeks1, indeks2])
    return result


def zapisz(param: str, wyniki: list[str]) -> None:
    with open(param, 'w') as file:
        file.write('\n'.join(wyniki))


if __name__ == '__main__':
    dane_1 = wczytaj_dane(r'.\dane_2018\NM_DANE_PR\dane1.txt')
    dane_2 = wczytaj_dane(r'.\dane_2018\NM_DANE_PR\dane2.txt')
    print(dane_2)
    ilosc_takich_samych_ostatnich = policz_takie_same_ostatnie(dane_1, dane_2)
    print(ilosc_takich_samych_ostatnich)
    ilosc_ciagow_z_parzystymi_i_nieparzystymi = policz_ilosc_ciagow_z_parzystymi_i_nieparzystymi(dane_1, dane_2)
    print(ilosc_ciagow_z_parzystymi_i_nieparzystymi)
    ilosc_ciagow_z_tych_samych_liczb = policz_ilosc_ciagow_z_tych_samych_liczb(dane_1, dane_2)
    print(ilosc_ciagow_z_tych_samych_liczb)
    wyniki = []
    wyniki.append('zad4.1')
    wyniki.append(ilosc_ciagow_z_tych_samych_liczb)
    wyniki.append('zad4.2')
    wyniki.append(ilosc_ciagow_z_parzystymi_i_nieparzystymi)
    wyniki.append('zad4.3')
    wyniki.append(ilosc_ciagow_z_tych_samych_liczb)
    zapisz(r'.\dane_2018\NM_DANE_PR\wyniki.txt', wyniki)