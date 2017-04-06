container = [
    ['A', 'P', 'O', 'R', 0],
    ['B', 'M', 'S', 1],
    ['D', 'G', 'J', 'K', 'T', 'W', 2]
]

count_msg = int(input())
recepient = []

while count_msg > 0:
    recepient.append(str(input()))
    count_msg -= 1

step = 0
position = 0

for human in recepient:
    if human[0] in container[0]:
        step += abs(position - int(container[0][-1]))
        position = 0
        continue
    if human[0] in container[1]:
        step += abs(position - int(container[1][-1]))
        position = 1
        continue
    if human[0] in container[2]:
        step += abs(position - int(container[2][-1]))
        position = 2
        continue

print(step)
