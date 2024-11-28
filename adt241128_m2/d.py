N = int(input())
S = [input() for _ in [0] * N]

win = [[0, i + 1] for i in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == 'o':
            win[i][0] -= 1
win.sort()

print(*[win[i][1] for i in range(N)])