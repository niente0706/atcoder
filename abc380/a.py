N = input()

count = [0] * 10
for i in range(len(N)):
    count[int(N[i])] += 1

if count[1] == 1 and count[2] == 2 and count[3] == 3:
    print('Yes')
else:
    print('No')