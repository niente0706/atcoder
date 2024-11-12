N = int(input())
A = list(map(int, input().split()))

acc = [A[0]]
i = 1
while i < N:
    if A[i] == acc[-1]:
        i += 1
    elif A[i] < acc[-1]:
        acc.append(acc[-1] - 1)
    else:
        acc.append(acc[-1] + 1)
print(*acc)