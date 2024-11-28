N = int(input())
X, Y = map(int, input().split())
Boxes = [list(map(int, input().split())) for _ in range(N)]

inf = 10 ** 18
dp = [[[inf] * (Y + 1) for _ in [0] * (X + 1)] for __ in [0] * (N + 1)]
dp[0][0][0] = 0
for i in range(N):
    xi, yi = Boxes[i]
    for x in range(X + 1):
        for y in range(Y + 1):
            b = dp[i][x][y]
            if b == inf:
                continue
            if dp[i + 1][x][y] > b:
                dp[i + 1][x][y] = b
            nextx = min([X, x + xi])
            nexty = min([Y, y + yi])
            if dp[i + 1][nextx][nexty] > b + 1:
                dp[i + 1][nextx][nexty] = b + 1

ans = dp[N][X][Y]
if ans == inf:
    print(-1)
else:
    print(ans)