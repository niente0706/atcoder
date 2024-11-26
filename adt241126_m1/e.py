from collections import defaultdict

N = int(input())
S = [input() for _ in [0] * N]

acc = [[] for _ in [0] * 10]
for i in range(N):
    for j in range(10):
        x = int(S[i][j])
        acc[x].append(j)

ans = 10 ** 18
for i in range(10):
    A = acc[i]
    count = defaultdict(int)
    for j in range(N):
        count[A[j]] += 1
    maxpop = []
    maxcount = -1
    for j in count:
        if count[j] == maxcount:
            maxpop.append(j)
        elif count[j] > maxcount:
            maxcount = count[j]
            maxpop = [j]
    ans = min(ans, (maxcount - 1) * 10 + max(maxpop))

print(ans)