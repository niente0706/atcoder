S = input()
T = input()
N = len(S)
ceil = ord('z')
Schar = [ord(S[i]) for i in range(N)]

for i in range(26):
    schar = Schar[0] + i
    if schar > ceil:
        schar -= 26
    if chr(schar) == T[0]:
        for j in range(1, N):
            schar = Schar[j] + i
            if schar > ceil:
                schar -= 26
            if chr(schar) != T[j]:
                print('No')
                exit()
        print('Yes')