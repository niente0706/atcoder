from bisect import bisect_left

H, W, N = map(int, input().split())
C = [list(map(int, input().split())) for _ in [0] * N]

row = set()
col = set()
for i in range(N):
    r, c = C[i]
    row.add(r)
    col.add(c)
rsort = sorted(row)
csort = sorted(col)

for i in range(N):
    ir = bisect_left(rsort, C[i][0])
    ic = bisect_left(csort, C[i][1])
    print(ir + 1, ic + 1)