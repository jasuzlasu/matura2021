def czy_pierwsza(param) -> bool:

    if param == 2:
        return True
    jest_pierwsza = False
    for i in range(2, param):
        if param % i == 0:
            return False
        else:
            jest_pierwsza = True
    return jest_pierwsza



if __name__ == '__main__':
    param = 54
    print(czy_pierwsza(param))