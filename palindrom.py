def is_palindrom(napis):
    return napis == napis[::-1]
    # if napis == napis[::-1]:
    #     return True
    # else:
    #     return False

if __name__ == "__main__":
    # palindrom('kajak')
    is_palindrom('kak')

    # palindrom('kjhjkhjjk')
