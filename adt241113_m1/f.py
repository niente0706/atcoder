N, K = map(int, input().split())
S = [input() for _ in [0] * N]
base = ord('a')

ans = 0
for i in range(1 << N):
    acc = [0] * 26
    for j in range(N):
        if i >> j & 1:
            s = S[j]
            for k in range(len(s)):
                acc[ord(s[k]) - base] += 1
    xcount = 0
    for x in range(26):
        if acc[x] == K:
            xcount += 1
    ans = max(ans, xcount)

print(ans)