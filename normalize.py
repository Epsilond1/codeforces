string = str(input())
final_str = ''
iter = -1

string = string.lstrip(' ')
string = string.rstrip(' ')

for i in string.split(' '):
    if len(final_str) > 0:
        if i == '' and final_str[-1] == ' ':
            del i
            continue
    if i != '':
        final_str += i
    else:
        final_str += ' '
    iter += 1

print(final_str)
