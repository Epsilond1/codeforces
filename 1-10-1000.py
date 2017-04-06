n = int(input())
sequence = []
final_sequence = [1, 1]
i = n

while i > 0:
    sequence.append(int(input()))
    i -= 1

i = 1
while i <= n:
    buf = i
    while buf > 0:
        final_sequence.append(0)
        buf -= 1
    final_sequence.append(1)
    i += 1

for num in sequence:
    print(final_sequence[num-1])
