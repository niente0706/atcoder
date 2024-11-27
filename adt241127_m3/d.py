N = int(input())
B = [list(map(int, input().split())) for _ in [0] * N]

ans = 0
for t in range(24):
    attend = 0
    for i in range(N):
        if 9 <= (t + B[i][1]) % 24 < 18:
            attend += B[i][0]
    ans = max([ans, attend])

print(ans)