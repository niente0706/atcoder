N, K = map(int, input().split())
S = input()

ans = [S[0]]
acc = []
last = S[0]
count = int(S[0])
for i in range(1, N):
    if S[i] != S[i - 1]:
        if S[i] == '1':
            count += 1
        elif count == K:
            ans += acc
            acc = []
    if count == K - 1 and S[i] == '0':
        acc.append('0')
        continue
    ans.append(S[i])
if acc:
    ans += acc

print(''.join(ans))