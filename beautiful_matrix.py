import math


def getcoord(matrix):
    coord = [-1, -1]
    i = 1
    j = 1
    for rows in matrix:
        j = 1
        for columns in rows:
            if columns == 1:
                coord[0] = i
                coord[1] = j
                return coord
            j += 1
        i += 1

i = 0
matrix = []

while i < 5:
    matrix.append([int(x) for x in input().split(' ')])
    i += 1

coord = getcoord(matrix)

print(int(math.fabs(coord[0] - 3) + math.fabs(coord[1] - 3)))
