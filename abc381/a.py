N = int(input())
S = input()

if N % 2 == 0:
    print('No')
    exit()
for i in range(N // 2):
    if (S[i] != '1') or (S[-i - 1] != '2'):
        print('No')
        exit()
if S[N // 2] != '/':
    print('No')
else:
    print('Yes')