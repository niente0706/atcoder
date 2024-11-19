T = int(input())
for _ in [0] * T:
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] & 1:
            ans += 1
    print(ans)