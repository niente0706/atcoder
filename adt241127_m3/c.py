N = int(input())
A = set(map(int, input().split()))
X = sorted(A)
i = 0
while i < len(X) and i == X[i]:
    i += 1
print(i)