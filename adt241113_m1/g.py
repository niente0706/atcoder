from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
accA = [0]
for i in range(N):
    accA.append(accA[-1] + A[i])

acc_x = defaultdict(int)
for i in range(N + 1):
    acc_x[accA[i]] += 1

ans = 0
for i in range(N):
    r = accA.pop()
    acc_x[r] -= 1
    x = r - K
    ans += acc_x[x]

print(ans)