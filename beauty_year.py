year = int(input()) + 1

def isbeauty(year):
    nyear = str(year)
    nyear = sorted(nyear)
    return nyear[0] != nyear[1] != nyear[2] != nyear[3]

while True:
    if isbeauty(year):
        break
    year += 1

print(year)
