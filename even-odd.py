n, k = [int(x) for x in input().split(' ')]
if k <= n//2:
    print([int(x) for x in range(1, n, 2)][k-1])
elif k > n//2 and k < n:
    print([int(x) for x in range(2, n, 2)][k - n//2 - 1])
else:
    print([int(x) for x in range(2, n, 2)][k-n//2-1])