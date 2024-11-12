N = int(input())
S = input()

numbers = [0] * 10
for i in range(N):
    numbers[int(S[i])] += 1

if N % 2 == 1:
    flag = True
    digit = N + 1
    numbers[0] += 1
else:
    flag = False
    digit = N

ans = 0
for i in range(10 ** (digit // 2)):
    x = str(i * i).zfill(digit)
    if flag and x[0] != '0':
        continue
    num = [0] * 10
    for j in range(digit):
        num[int(x[j])] += 1
    if num == numbers:
        ans += 1

print(ans)