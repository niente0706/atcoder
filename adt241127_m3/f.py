K = int(input())

Kbit = []
j = 0
while (1 << j) <= K:
    if (K >> j) & 1:
        Kbit.append(j)
    j += 1

ans = ['0'] * j
for i in Kbit:
    ans[i] = '2'

print(''.join(ans[::-1]))