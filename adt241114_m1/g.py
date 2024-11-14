N = int(input())
S = input()

ans = [0] * (N + 1)
left = 0
right = N
for i in range(N):
    if S[i] == 'L':
        ans[right] = i
        right -= 1
    else:
        ans[left] = i
        left += 1
ans[left] = N

print(*ans)