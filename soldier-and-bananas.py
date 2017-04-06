k, n, w = [int(x) for x in input().split(' ')]

sum = 0
while w > 0:
    sum += (k * w)
    w -= 1

if sum - n > 0:
    print(sum - n)
else:
    print(0)

