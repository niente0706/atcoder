N, M, H, K = map(int, input().split())
S = input()
Heal = set([tuple(map(int, input().split())) for _ in [0] * M])
move = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}

pos = (0, 0)
i = 0
while i < N:
    if H == 0:
        print('No')
        exit()
    H -= 1
    pos = (pos[0] + move[S[i]][0], pos[1] + move[S[i]][1])
    if H < K and pos in Heal:
        Heal.discard(pos)
        H = K
    i += 1

print('Yes')