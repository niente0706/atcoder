N, M = map(int, input().split())
G = [[0] * N for _ in [0] * N]
for _ in [0] * M:
    A, B, C = map(int, input().split())
    G[A - 1][B - 1] = C
    G[B - 1][A - 1] = C

ans = 0
visited = [False] * N
def rec(u, c):
    global ans
    if c > ans:
        ans = c
    visited[u] = True
    for v in range(N):
        if not visited[v] and G[u][v]:
            rec(v, c + G[u][v])
    visited[u] = False

for i in range(N):
    rec(i, 0)

print(ans)