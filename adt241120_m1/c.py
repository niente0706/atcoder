S = input()
T = input()

N = len(S)
if T[:N] == S:
    print('Yes')
else:
    print('No')