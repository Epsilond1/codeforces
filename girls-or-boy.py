def getmetrics(name):
    cname = ''
    for sym in name:
        if cname.find(sym) == -1:
            cname += sym
    return len(cname)

name = str(input())
count = getmetrics(name)

if count % 2 != 0:
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')

