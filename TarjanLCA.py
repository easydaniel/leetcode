n = 10
adj = [[1 if j == i else 0 for i in range(n)] for j in range(n)]
parent = [i for i in range(n)]
walked = [False for _ in range(n)]
lca = [[0 for _ in range(n)] for _ in range(n)]


def find(r):
    if r == parent[r]:
        return r
    parent[r] = find(parent[r])
    return parent[r]

def dfs(r):
    if walked[r]:
        return
    walked[r] = True
    for j in range(n):
        if walked[j]:
            lca[r][j], lca[j][r] = find(j)
    for j in range(n):
        if adj[r][j]:
            dfs(j)
            parent[j] = r
