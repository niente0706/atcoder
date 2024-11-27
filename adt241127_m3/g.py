N = int(input())
A = list(map(int, input().split()))

stack = []
ans = 0
for i in range(N):
    ans += 1
    if stack and stack[-1][0] == A[i]:
        stack[-1][1] += 1
        if stack[-1][1] == stack[-1][0]:
            ans -= stack[-1][1]
            stack.pop()
    else:
        stack.append([A[i], 1])
    print(ans)