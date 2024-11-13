N, X = map(int, input().split())
A = list(map(int, input().split()))

known = [0] * N
x = X - 1
while known[x] == 0:
    known[x] = 1
    x = A[x] - 1
print(sum(known))