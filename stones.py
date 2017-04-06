count = int(input())
colors = [x for x in input()]

i = 0
deleted = 0
buf = colors[i]
i += 1

while i < count:
    if colors[i] == buf:
        deleted += 1
    else:
        buf = colors[i]
    i += 1

print(deleted)
