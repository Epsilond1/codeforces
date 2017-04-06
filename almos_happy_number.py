num = str(input())
table = [4, 7, 44, 47, 477, 474, 447, 747, 744, 774]

count = 0

for n in num:
    if int(n) in table:
        count += 1

if count == 4 or count == 7:
    print('YES')
else:
    print('NO')
