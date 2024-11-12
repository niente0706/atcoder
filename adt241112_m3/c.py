S, T = input().split()

for i in range(len(S) - 1):
    l = i + 1
    for j in range(l):
        s = S[j::l]
        if s == T:
            print('Yes')
            exit()
print('No')