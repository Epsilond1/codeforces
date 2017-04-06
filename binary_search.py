def binary_search(A, l, r, k):
    ans = None
    if l < r:
        pivot = (l+r) // 2
        if A[pivot] == k:
            ans = pivot
        elif k > A[pivot]:
            return binary_search(A, pivot+1, r, k)
        elif k < A[pivot]:
            return binary_search(A, l, pivot, k)
    return ans


def stresstest(A):
    print(A)
    for a in A:
        print(binary_search(A, 0, len(A), a))


A = [int(x) for x in input().split(' ')]
key = int(input())

print(binary_search(sorted(A), 0, len(A), key))
