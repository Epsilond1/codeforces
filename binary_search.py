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


def tests():
    print(binary_search([1, 2, 3, 4], 0, 4, 4) == 3)  # ok
    print(binary_search([1, 2, 3, 4], 0, 4, 5) == None)  # no exists element
    print(binary_search([1, 3, 5, 7, 9], 0, 5, 9) == 4)
    print(binary_search([1, 3, 5, 7, 9], 0, 5, 1) == 0)
    print(binary_search([1, 3, 5, 7, 9], 0, 5, 5) == 2)
    print(binary_search([1, 1, 1, 1, 1], 0, 5, 1) == 2)


# A = sorted([int(x) for x in input().split(' ')])
# key = int(input())
tests()
# print(binary_search(sorted(A), 0, len(A), key))

