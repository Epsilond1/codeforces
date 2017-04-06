queue = ['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']

number = int(input())

if number <= 5:
    print(queue[number-1])
else:
    pwr = 0
    while 5*(2**pwr) <= number:
        pwr += 1
    