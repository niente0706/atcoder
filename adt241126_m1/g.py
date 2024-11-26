A, B = map(int, input().split())
if A == B:
    print(0)
    exit()

ans = 0
while A != B and A > 0 and B > 0:
    if A > B:
        ans += A // B
        A = A % B
    else:
        ans += B // A
        B = B % A

print(ans - 1)