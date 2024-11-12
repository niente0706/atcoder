N, M = map(int, input().split())
S = [input() for _ in [0] * N]

ans = 20
for i in range(1 << N):
    stores = 0
    popcorns = [False] * M
    for j in range(N):
        if i >> j & 1:
            stores += 1
            s = S[j]
            for l in range(M):
                if s[l] == 'o':
                    popcorns[l] = True
    if all(popcorns):
        ans = min(ans, stores)
print(ans)