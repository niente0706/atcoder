N, Q = map(int, input().split())
Query = [input().split() for _ in [0] * Q]
move = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}

pos = [[i, 0] for i in range(N, 0, -1)]
for q, x in Query:
    if q == '1':
        head = pos[-1]
        pos.append([head[0] + move[x][0], head[1] + move[x][1]])
    else:
        print(*pos[-int(x)])