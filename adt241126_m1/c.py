S = input()
T = input()
if len(S) != len(T):
    print('No')
    exit()
N = len(S)
if S == T:
    print('Yes')
    exit()

for i in range(N - 1):
    s = S[:i] + S[i + 1] + S[i] + S[i + 2:]
    if s == T:
        print('Yes')
        exit()
print('No')