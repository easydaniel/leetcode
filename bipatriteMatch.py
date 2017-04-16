class bipartiteMatch(object):

    def __init__(self, graph):
        self.graph = graph
        self.xlen = len(graph)
        self.ylen = len(graph[0])

    def bpm(self, idx, match, visit):
        for jdx in range(self.ylen):
            if self.graph[idx][jdx] == 1 and not visit[jdx]:
                visit[jdx] = True
                if match[jdx] == -1 or self.bpm(match[jdx], match, visit):
                    match[jdx] = idx
                    return True
        return False

    def maxBPM(self):
        result = 0
        match = [-1] * self.ylen
        for idx in range(self.xlen):
            visit = [False] * self.ylen
            if self.bpm(idx, match, visit):
                result += 1
        return match, result


g = [[0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1]]

for idx, row in enumerate(g):
    for jdx, c in enumerate(row):
        if c == 1:
            print((idx, jdx))

bm = bipartiteMatch(g)
print(bm.maxBPM())
