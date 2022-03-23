def wczytaj_dane(param:str) ->list[list[str]]:
    with open(param) as file:
        file = file.readlines()
    return [linia.split() for linia in file]


def szukaj_takich_samych_ostatnich(dane1: list[list[str]], dane2: list[list[str]]) -> int:
    result = 0
    for linia1, linia2 in zip(dane1, dane2):
        if linia1[-1] == linia2[-1]:
            result += 1
    return result


def jest_parzysta(element:str) -> bool:
    return int(element) % 2 == 0


def jest_5_parzystych_i_nieparzystych(linia1: list[str]) -> bool:
    parzyste = 0
    nieparzyste = 0
    for element in linia1:
       if element == '0':
           return False
       if jest_parzysta(element):
           parzyste += 1
       else:
           nieparzyste += 1
    return parzyste == 5 and nieparzyste == 5



def szukaj_5_parzystych_i_nieparzystych(dane1: list[list[str]], dane2: list[list[str]]) -> int:
    result = 0
    for linia1, linia2 in zip(dane1, dane2):
        if jest_5_parzystych_i_nieparzystych(linia1) and jest_5_parzystych_i_nieparzystych(linia2):
            result += 1
    return result


def szukaj_ciagow_z_takich_samych_liczb(dane1: list[list[str]], dane2: list[list[str]]) -> int:
    result = 0
    for ciag1, ciag2 in zip(dane1, dane2):
        if set(ciag1) == set(ciag2):
            result += 1
    return result


def scal_ciagi(ciag1: list[str], ciag2: list[str]) -> list[str]:
    result = []
    for element1 in ciag1:
        element1 = int(element1)
        for element2 in ciag2:
            element2 = int(element2)
            if element1 <= element2:
                result.append(element1)
            else:
                result.append(element2)





    return result


def scal(dane1: list[list[str]], dane2: list[list[str]]) -> list[list[str]]:
    result = []
    for ciag1, ciag2 in zip(dane1, dane2):
        result.append(scal_ciagi(ciag1, ciag2))





    return result



if __name__ == '__main__':
    dane1 = wczytaj_dane(r'.\dane_2018\NM_DANE_PR\dane1.txt')
    dane2 = wczytaj_dane(r'.\dane_2018\NM_DANE_PR\dane2.txt')
    print(dane1)
    print(szukaj_takich_samych_ostatnich(dane1, dane2))
    print(szukaj_5_parzystych_i_nieparzystych(dane1, dane2))
    print(szukaj_ciagow_z_takich_samych_liczb(dane1, dane2))
    scal(dane1, dane2)