N = int(input())
S = [input() for _ in [0] * N]
T = [input() for _ in [0] * N]

Shash = []
Thash = set()
for i in range(N):
    for j in range(N):
        if S[i][j] == '#':
            Shash.append((i, j))
        if T[i][j] == '#':
            Thash.add((i, j))

if len(Shash) != len(Thash):
    print('No')
    exit()

for _ in range(4):
    for i in range(-N, N):
        for j in range(-N, N):
            flag = True
            for x, y in Shash:
                moved = (x + i, y + j)
                if not (0 <= moved[0] < N and 0 <= moved[1] < N and moved in Thash):
                    flag = False
                    break
            if flag:
                print('Yes')
                exit()
    for x in range(len(Shash)):
        i, j = Shash[x]
        Shash[x] = (j, N - i - 1)

print('No')