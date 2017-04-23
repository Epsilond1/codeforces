array = [int(x) for x in range(0, 100)]
del array[99]
print(sum([int(x) for x in range(0, 100)]) - sum(array))
