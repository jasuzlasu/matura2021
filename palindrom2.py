from itertools import combinations, permutations
napis = '1212'


def jest_palindromem(i: tuple[str]) -> bool:
    i = list(i)
    return i == i[::-1]


def czy_moze_byc_palindromem(napis: str) -> bool:
    for i in permutations(napis, len(napis)):
        if jest_palindromem(i):
            return True
    return False




if __name__ == '__main__':
    print(czy_moze_byc_palindromem(napis))
    print('\a')
    import winsound

    winsound.Beep(500, 500)
