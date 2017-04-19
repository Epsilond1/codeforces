import math


def getfibball(count):
    fibb = []
    while count >= 1:
        fibb.append(getfibn(count))
        count -= 1
    return reversed(fibb)


def getfibn(n):
    sqrt = math.sqrt(5)
    return round((((1 + sqrt) / 2) ** n - (1 - sqrt) / 2 ** n) / sqrt)


def getfibcicle(n):
    fibb = [0, 1]
    i = 1
    while i < n:
        fibb.append(fibb[0] + fibb[1])
        i += 1
        del fibb[0]
    return fibb[-1]


def get_last_digin(n):
    return n % 10

n = int(input())
print(get_last_digin(getfibcicle(n)))
