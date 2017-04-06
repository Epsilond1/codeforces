def write(A, i):
    if i < len(A) - 1:
        write(A, i + 1)
    print(A[i])


lst = list(input().split(' '))
write(lst, 0)
