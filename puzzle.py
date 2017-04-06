student, psize = [int(x) for x in input().split(' ')]

puzzless = [int(x) for x in input().split(' ')]
puzzless.sort()

best = puzzless[-1]

i = 0
while i <= psize - student:
    best = min(best, puzzless[i+student-1] - puzzless[i])
    i += 1
print(best)
