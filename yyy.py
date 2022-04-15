from collections import Counter


def najdluzsza(napis: str) -> list[str, int]:
    result = [[napis[0], 1]]

    for indeks, litera in enumerate(napis):
        if indeks < len(napis) - 1:
            if litera == napis[indeks + 1]:
                result[-1][1] += 1
            else:
                result.append([napis[indeks + 1], 1])
    maks = 0
    maks_litera = None

    for litera, liczba in result:
        if liczba > maks:
            maks = liczba
            maks_litera = litera

    return [maks_litera, maks]


def czy_anagram(napis: str, napis2: str) -> bool:
    print(Counter(napis))
    return Counter(napis) == Counter(napis2)



if __name__ == '__main__':
    napis = 'aabcb'
    napis2 = 'aabc'

    print(najdluzsza(napis))
    print(czy_anagram(napis, napis2))