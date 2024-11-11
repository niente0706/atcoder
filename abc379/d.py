import bisect

Q = int(input())
Query = [list(map(int, input().split())) for _ in [0] * Q]

acc = []
last = 0
T = 0
for q in Query:
    if q[0] == 1:
        acc.append(T)
    elif q[0] == 2:
        T += q[1]
    else:
        cut = T - q[1]
        icut = bisect.bisect_right(acc, cut)
        print(icut - last)
        last = icut
