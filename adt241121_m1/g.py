N = int(input())
A = list(map(int, input().split()))
mod = 998244353

ans = 0
for m in range(1, N + 1):
    dp = [[[0] * m for _ in range(m + 1)] for __ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(m + 1):
            for k in range(m):
                dp[i + 1][j][k] += dp[i][j][k]
                if j < m:
                    dp[i + 1][j + 1][(k + A[i - 1]) % m] += dp[i][j][k]
    ans += dp[N][m][0]

print(ans % mod)