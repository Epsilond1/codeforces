def parse(cmnd):
    result = ""
    for sym in cmnd:
        if sym == 'H':
            result += 'Hello, World!'
        elif sym == 'Q':
            result += cmnd
        elif sym == '9':
            result += '99 бутылок пива'
        elif sym == '+':
            continue
    return result

command = str(input())
answer = parse(command)
if answer != "":
    print('YES')
else:
    print('NO')

