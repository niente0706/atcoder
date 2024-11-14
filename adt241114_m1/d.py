N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans0 = 0
accA = set()
accB = set()
for i in range(N):
    a = A[i]
    b = B[i]
    accA.add(a)
    accB.add(b)
    if a == b:
        ans0 += 1

ans1 = len(accA & accB) - ans0
print(ans0)
print(ans1)