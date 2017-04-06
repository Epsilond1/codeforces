def parse_string(word):
    alphabet = ['h', 'e', 'l', 'l', 'o']
    parse = ''
    for b in word:
        if b in alphabet:
            parse += b
    return parse


def pretest(word):
    alphabet = ['h', 'e', 'l', 'l', 'o']
    position = []
    i = 0
    j = 0
    answer = ''
    while i < len(alphabet):
        letter = alphabet[i]
        while j < len(word):
            if word[j] == letter and (not j in position):
                answer += letter
                position.append(j)
                break
            j += 1
        i += 1
    return answer

word = str(input())

answer = pretest(parse_string(word))
if answer == 'hello':
    print('YES')
else:
    print('NO')
