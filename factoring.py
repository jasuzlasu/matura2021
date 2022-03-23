n = 1025
def jest_pierwsza(x: int) -> bool:
    if x == 0 or x == 1 or x % 2 == 0:
        return False
    elif x == 2:
        return True
    else:
        for i in range(3, x, 2):
            if x % i == 0:
                return False
    return True

def faktoryzuj(n: int) -> list[int]:
    result = []
    for i in range(2, n):
        while n % i == 0:
            result.append(i)
            n = n / i
    return result

if __name__ == '__main__':
    print(faktoryzuj(n))
    print(jest_pierwsza(n))