def waga(param: int) -> int:
    param = list(str(param))
    while len(param) > 1:
        suma = 0
        for element in param:
            suma += int(element)
        param = list(str(suma))
    return suma


def podzielne_przez_3(x: list[str]) -> list[str]:
    result = []
    for element in x:
        if int(element, 2) % 3 == 0:
            result.append(element)

    return result


def podzielne_przez_n(x: list[str], n: int) -> list[str]:
    result = []
    for element in x:
        if int(element, 2) % n == 0:
            result.append(element)
    return result

if __name__ == '__main__':
    print(waga(31699))

    x = ['1001010010', '110110', '1111']
    y = [element for element in x if element[-1] == '0']
    z = [element for element in x if int(element, 2) % 3 == 0]
    print(y)
    print(z)
