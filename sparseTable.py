from math import log, ceil, floor

class sparseTable(object):

    def __init__(self, s):
        self.s = [[value if row == 0 else 0 for value in s] for row in range(ceil(log(len(s), 2)))]
        idx = 1
        while (1 << idx) <= len(s):
            jdx = 0
            while jdx + (1 << idx) <= len(s):
                self.s[idx][jdx] = min(self.s[idx - 1][jdx], self.s[idx - 1][jdx + (1 << (idx - 1))])
                jdx += 1
            idx += 1

    def query(self, a, b):
        search = floor(log(abs(b - a) + 1, 2))
        return min(self.s[search][a], self.s[search][b - (1 << search) + 1])

st = sparseTable([10, 25, 22, 7, 34, 2, 9, 12, 16, 16])
print(st.query(1, 7))
print(st.query(0, 9))
