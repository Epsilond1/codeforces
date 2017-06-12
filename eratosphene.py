import math


class Sieve(object):
    def __init__(self, value):
        self.value = value
        self.flag = True


count = int(input())
arrays = [Sieve(x) for x in range(2, count+1)]

index = 0
step = 1
while index <= math.sqrt(len(arrays)) + 1:
    if arrays[index].flag == False:
        index += 1
        continue
    iterator = index + step
    while iterator < len(arrays):
        if arrays[iterator].value % arrays[index].value == 0:
            arrays[iterator].flag = False
        iterator += step
    index += 1


for element in arrays:
    if element.flag == True:
        print(element.value)
