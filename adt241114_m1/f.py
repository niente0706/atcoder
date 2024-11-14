from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

color_acc = defaultdict(int)
for i in range(N):
    color_acc[A[i]] += 1

ans = 0
for c in color_acc:
    ans += color_acc[c] // 2

print(ans)