def build(s):
    fail = [-1]
    i, j = 1, -1
    while i < len(s):
        while j >= 0 and s[j + 1] != s[i]:
            j = fail[j]
        if s[j + 1] == s[i]:
            j += 1
        fail.append(j)
        i += 1
    return fail

def match(s, p, f):
    m = []
    i, j = 0, -1
    while i < len(s):
        while j >= 0 and p[j + 1] != s[i]:
            j = f[j]
        if p[j + 1] == s[i]:
            j += 1
        if j == len(p) - 1:
            m.append(i - len(p) + 1)
            j = f[j]
        i += 1
    return m

s = 'abcasdfmioweabcasd'
p = 'abc'
f = build(p)
print(match(s, p, f))
