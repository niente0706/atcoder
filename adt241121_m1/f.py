from itertools import combinations

N = int(input())
P = [list(map(int, input().split())) for _ in [0] * N]

ans = 0
for c in combinations(P, 3):
    p1, p2, p3 = c
    if (p1[0] - p2[0]) * (p1[1] - p3[1]) == (p1[0] - p3[0]) * (p1[1] - p2[1]):
        continue
    ans += 1

print(ans)