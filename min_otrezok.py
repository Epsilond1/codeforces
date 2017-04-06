def getindexes(A):
    ans = 0
    add = 0
    min_add = 0
    l = r = 1
    rans = lans = 0
    for i in A:
        add += i
        ans = max(ans, add - min_add)
        min_add = min(min_add, add)
    return lans, rans


line = [int(x) for x in input().split(' ')]
print(getindexes(line))
