N = int(input())
S = [list(map(int, input().split())) for _ in [0] * N]

acc = set()
for i in range(N):
    A, B, C, D = S[i]
    for x in range(A, B):
        for y in range(C, D):
            cell = (x, y)
            acc.add(cell)

print(len(acc))