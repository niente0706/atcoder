N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

Stones = sorted(zip(X, A), key=lambda x: x[0])
Stones.append([N + 1, 0])
M += 1

ans = 0
pos = 0
acc = 1
for i in range(M):
    d = Stones[i][0] - pos
    if acc < d:
        print(-1)
        exit()
    carryover = acc - d
    ans += d * (acc - 1 + carryover) // 2
    pos += d
    acc = carryover + Stones[i][1]

if acc != 0:
    print(-1)
else:
    print(ans)