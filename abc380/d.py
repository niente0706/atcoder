S = input()
N = len(S)
Q = int(input())
K = [int(x) - 1 for x in input().split()]

def mode(x):
    i = x % N
    m = (x // N).bit_count() % 2
    return i, m

ans = []
for q in range(Q):
    i, m = mode(K[q])
    c = S[i]
    if m:
        if c == c.upper():
            ans.append(c.lower())
        else:
            ans.append(c.upper())
    else:
        ans.append(c)

print(*ans)