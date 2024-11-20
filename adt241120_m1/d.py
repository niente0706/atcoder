H, W = map(int, input().split())
S = [input() for _ in [0] * H]

komas = []
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            komas.append([i, j])

dist = (komas[1][0] - komas[0][0]) + abs(komas[1][1] - komas[0][1])
print(dist)