def prefix(s):
    pi = []
    i = 0
    while i < len(s):
        k = 0
        pi.append(k)
        while k <= i:
            if s[0:k] == s[i-k+1:i]:
                pi[i] = k
            k += 1
        i += 1
    return pi

str = str(input())
print(prefix(str))
