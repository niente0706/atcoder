N = int(input())
A = set()
for _ in [0] * N:
    L, *a = map(int, input().split())
    A.add(tuple(a))

print(len(A))