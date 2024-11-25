S = input()
N = len(S)
if N % 2 == 1:
    print('No')
    exit()

acc = [0] * 26
base = ord('a')
for i in range(N):
    if i % 2 == 0 and S[i] != S[i + 1]:
        print('No')
        exit()
    acc[ord(S[i]) - base] += 1

for i in range(26):
    if acc[i] != 0 and acc[i] != 2:
        print('No')
        exit()

print('Yes')