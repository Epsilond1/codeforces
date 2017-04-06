'''
Random-Select
'''


def partition(A, l, r):
    i = l
    j = r
    pivot = A[(l+r)//2]

    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            buf = A[i]
            A[i] = A[j]
            A[j] = buf
            i += 1
            j -= 1

    return i


def getorderstatistic(A, l, r, k):
    if l <= r-1:
        index = partition(A, l, r)
        if k < index:
            getorderstatistic(A, l, index - 1, k)
        if k >= index:
            getorderstatistic(A, index, r, k)

    return A[k]


def getkmaxelement(A, l, r, k):
    if l <= r-1:
        index = partition(A, l, r)
        if k < index:
            getkmaxelement(A, l, index-1, k)
        if k >= index:
            getkmaxelement(A, index, r, k)
    return A

S = [int(x) for x in input().split(' ')]
k = int(input())

print(getorderstatistic(S, 0, len(S) - 1, k - 1))
#print(getkmaxelement(S, 0, len(S) - 1, k)[-k:])
print(sorted(S))
