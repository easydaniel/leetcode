class BIT(object):

    def __init__(self, size):
        self.s = [0 for _ in range(size + 1)]
        self.size = size

    def add(self, idx, value):
        # print(f'add: {idx} {value}')
        while idx <= self.size:
            # print(idx)
            self.s[idx] += value
            idx += (idx & -idx)

    def rangeSum(self, idx):
        total = 0
        while idx > 0:
            total += self.s[idx]
            idx -= (idx & -idx)
        return total

    def query(self, a, b):
        if a > b:
            a, b = b, a

        return self.rangeSum(b) - self.rangeSum(a - 1) if a != 0 else self.rangeSum(b)

bit = BIT(10)

for idx, value in enumerate([10, 25, 22, 7, 34, 2, 9, 12, 16, 16]):
    bit.add(idx + 1, value)

for prefix in bit.s[1:]:
    print(prefix)
