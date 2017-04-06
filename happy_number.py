def brute(table, num):
    for i in table:
        if num % i == 0:
            return True
    return False


num = int(input())
table = [4, 7, 47, 477, 474, 447, 747, 744, 774]

if brute(table, num):
    print('YES')
elif num in table:
    print('YES')
elif num % 4 == 0 and num % 7 == 0:
    print('YES')
else:
    print('NO')
