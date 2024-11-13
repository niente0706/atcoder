N = int(input())
A = list(map(int, input().split()))
B = sorted(zip(A, range(1, N + 1)), reverse=True, key=lambda x: x[0])
print(B[1][1])