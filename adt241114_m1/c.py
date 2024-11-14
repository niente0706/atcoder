N = int(input())
A = [list(map(int, input().split())) for _ in [0] * N]

ans = 0
for i in range(N):
    x = max(ans, i)
    y = min(ans, i)
    ans = A[x][y] - 1

print(ans + 1)