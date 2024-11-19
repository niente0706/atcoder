N = int(input())
A = list(map(int, input().split()))

ans = [[-2, i + 1] for i in range(N)]
for i in range(3 * N):
    x = A[i] - 1
    if ans[x][0] == -2:
        ans[x][0] = -1
    elif ans[x][0] == -1:
        ans[x][0] = i

ans.sort(key=lambda x: x[0])
print(*[ans[i][1] for i in range(N)])