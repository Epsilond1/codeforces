expression = [int(x) for x in input().split('+')]
expression.sort()
print('+'.join([str(x) for x in expression]))
