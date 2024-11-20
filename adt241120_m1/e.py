N = int(input())
A = [input() for _ in [0] * N]

B = [['.'] * N for _ in [0] * N]
for i in range(N):
    for j in range(N):
        if A[i][j] == '#':
            rot = min([i, N - i - 1, j, N - j - 1]) % 4
            if rot == 0:
                B[j][N - i - 1] = '#'
            elif rot == 1:
                B[N - i - 1][N - 1 - j] = '#'
            elif rot == 2:
                B[N - 1 - j][i] = '#'
            else:
                B[i][j] = '#'

for i in range(N):
    print(''.join(B[i]))