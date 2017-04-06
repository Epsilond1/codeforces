count = int(input())
i = 0
max = 0
current = 0

while i < count:
    passenger = [int(x) for x in input().split(' ')]
    current -= passenger[0]
    current += passenger[1]

    if current >= max:
        max = current

    i += 1

print(max)

