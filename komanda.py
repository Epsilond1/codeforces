n = int(input())
i = 0
tasks = []
solution_task = 0

while i < n:
    task = [int(x) for x in input().split(' ')]
    if sum(task) >= 2:
        solution_task += 1
    i += 1

print(solution_task)
