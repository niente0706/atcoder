N = int(input())
A = list(map(int, input().split()))

acc_cands = []
i = 0
while i < N - 1:
    if A[i] == A[i + 1]:
        if i < N - 2 and A[i] == A[i + 2]:
            i += 1
            continue
        acc_single = []
        while i < N - 1 and A[i] == A[i + 1]:
            acc_single.append(A[i])
            i += 2
        acc_cands.append(acc_single)
        if i < N and A[i] == A[i - 1]:
            i -= 1
    else:
        i += 1

ans = 0
while acc_cands:
    single = acc_cands.pop()
    n = len(single)
    acc_x = set()
    left = 0
    right = 0
    while right < n:
        if single[right] in acc_x:
            x = single[right]
            ans = max(ans, right - left)
            while x in acc_x:
                acc_x.discard(single[left])
                left += 1
        acc_x.add(single[right])
        right += 1
    ans = max(ans, right - left)

print(2 * ans)