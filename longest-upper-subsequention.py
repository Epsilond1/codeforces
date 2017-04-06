count = int(input())
seq = [int(x) for x in input().split(' ')]

it = 1
k = 1
res = 1

while it < count:
    if seq[it] >= seq[it-1]:
        k += 1
    else:
       res = max(res, k)
       k = 1
    it += 1

print(max(res, k))
