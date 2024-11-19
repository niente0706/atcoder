N, M = map(int, input().split())
A = [input() for _ in [0] * (2 * N)]
result = {
    ('G', 'G'): [0, 0], ('G', 'C'): [1, 0], ('G', 'P'): [0, 1],
    ('C', 'G'): [0, 1], ('C', 'C'): [0, 0], ('C', 'P'): [1, 0],
    ('P', 'G'): [1, 0], ('P', 'C'): [0, 1], ('P', 'P'): [0, 0]
}

win = [[0, i] for i in range(2 * N)]
for i in range(M):
    for j in range(N):
        a = win[2 * j][1]
        b = win[2 * j + 1][1]
        a_point, b_point = result[(A[a][i], A[b][i])]
        win[2 * j][0] += a_point
        win[2 * j + 1][0] += b_point
    win.sort(key=lambda x: [-x[0], x[1]])

ans = [0] * (2 * N)
for i in range(2 * N):
    print(win[i][1] + 1)