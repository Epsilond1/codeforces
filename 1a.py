import math
data = [int(x) for x in input().split(' ')]

n = data[0]
m = data[1]
a = data[2]

print(math.ceil(n / a) * math.ceil(m / a))
