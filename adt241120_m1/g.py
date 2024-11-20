from collections import deque

N = int(input())
S = list(input())
T = list(input())

sb = 0
tb = 0
for i in range(N):
    if S[i] == 'B':
        sb += 1
    if T[i] == 'B':
        tb += 1
if sb != tb:
    print(-1)
    exit()

N += 1
S += ['.']
T += ['.']

done = set()
deq = deque([[S, 0, N - 1]])
while deq:
    s, i, dots = deq.popleft()
    if s == T:
        print(i)
        exit()
    str = ''.join(s)
    if str in done:
        continue
    i += 1
    done.add(str)
    for j in range(N - 1):
        if (j == dots) or (j + 1 == dots):
            continue
        elif j < dots:
            next = s[:j] + ['.'] + s[j + 2 : dots] + s[j : j + 2] + s[dots + 1:]
            deq.append([next, i, j])
        else:
            next = s[:dots] + s[j : j + 2] + s[dots + 1 : j] + ['.'] + s[j + 2:]
            deq.append([next, i, j + 1])

print(-1)