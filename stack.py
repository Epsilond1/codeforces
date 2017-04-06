stack = []


def push(element):
    stack.append(element)


def top():
    return stack[-1]


def pop():
    a = stack.pop(-1)
    return a


push(1)
push(2)
push(3)

print(pop())
print(pop())

print(stack)
