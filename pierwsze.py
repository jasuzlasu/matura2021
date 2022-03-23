def czy_jest_pierwsza(param: int) ->bool:
    if param == 0 or param == 1:
        return False
    if param == 2:
        return True
    if param % 2 == 0:
        return False
    for i in range(3, param, 2):
        if param % i == 0:
            return False
    return True


if __name__ == '__main__':
    pass