element = [int(x) for x in input().split(' ')]

counter = {}

for el in element:
    if counter.get(el) == None:
        counter[el] = 1
    else:
        counter[el] += 1
count = list(set(sorted(counter.values())))
print(count[-2])
