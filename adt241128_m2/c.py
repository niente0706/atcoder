A, M, L, R = map(int, input().split())

L -= A
R -= A
ans = R // M - L // M
if L % M == 0:
    ans += 1

print(ans)