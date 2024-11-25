N = int(input())
S = input()

ans = 0
acc1 = 0
acc2 = 0
flag = 0
for i in range(N):
    if S[i] == '2':
        acc2 += 1
        acc1 = 0
    else:
        if flag > 0:
            ans = max(ans, min(flag, acc2))
            flag = 0
        acc2 = 0
        if S[i] == '1':
            acc1 += 1
        else:
            flag = acc1
            acc1 = 0

if flag > 0:
    ans = max(ans, min(flag, acc2))

print(2 * ans + 1)