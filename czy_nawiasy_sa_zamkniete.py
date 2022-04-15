
def czy_nawiasy_sa_zamkniete(napis: str) -> bool:
    from collections import Counter
    counter = Counter(napis)
    if counter['('] != counter[')'] and counter['['] != counter[']']:
        return False
    if napis[0] == ')' or napis[0] == ']':
        return False
    nawiasy = []
    for znak in napis:
        if znak == '(':
            nawiasy.append(znak)
        else:
            if not nawiasy:
                return False
            else:
                nawiasy.pop()
    return nawiasy == []





if __name__ == '__main__':
    napis = '()()()()()'
    print(czy_nawiasy_sa_zamkniete(napis))