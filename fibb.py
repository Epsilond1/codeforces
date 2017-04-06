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

n = int(input())
print(getfibball(n))
