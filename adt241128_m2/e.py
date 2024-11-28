N = int(input())
K = list(map(int, input().split()))
S = sum(K)

ans = 10 ** 18
for x in range(1 << N):
    a = 0
    for i in range(N):
        if x >> i & 1:
            a += K[i]
    ans = min([ans, max([a, S - a])])

print(ans)