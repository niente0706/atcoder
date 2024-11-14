N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

inf = 10 ** 18
imin = N
T.append(inf)
for i in range(N):
    if T[i] < T[imin]:
        imin = i

ans = [inf] * N
ans[imin] = T[imin]
for i in range(imin + 1, imin + N):
    j = i % N
    ans[j] = min([ans[j - 1] + S[j - 1], T[j]])

for i in range(N):
    print(ans[i])