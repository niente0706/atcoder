from copy import deepcopy
from itertools import permutations

Polyominos = []
for _ in [0] * 3:
    Polyomino = []
    P = [input() for _ in [0] * 4]
    corners = [4, 4, 0, 0]
    for i in range(4):
        for j in range(4):
            if P[i][j] == '#':
                corners = [min(corners[0], i), min(corners[1], j), max(corners[2], i), max(corners[3], j)]
    size = [corners[2] - corners[0] + 1, corners[3] - corners[1] + 1]
    
    Ponly = []
    for i in range(corners[0], corners[2] + 1):
        acc = []
        for j in range(corners[1], corners[3] + 1):
            acc.append(P[i][j])
        Ponly.append(acc)
    Polyomino.append(Ponly)
    for __ in range(3):
        P = Polyomino[-1]
        size = [len(P), len(P[0])]
        ponly = [['.'] * size[0] for ___ in [0] * size[1]]
        for i in range(size[0]):
            for j in range(size[1]):
                if P[i][j] == '#':
                    ponly[j][size[0] - i - 1] = '#'
        Polyomino.append(ponly)
    Polyominos.append(Polyomino)


def place_polyomino(start_i, start_j, p, g):
    size = [len(p), len(p[0])]
    j = 0
    while p[0][j] == '.':
        j += 1
    start_j -= j
    for i in range(size[0]):
        for j in range(size[1]):
            pos = [start_i + i, start_j + j]
            if pos[0] < 0 or 3 < pos[0] or pos[1] < 0 or 3 < pos[1]:
                return False
            cond1 = p[i][j] == '#'
            cond2 = g[pos[0]][pos[1]] == '#'
            if cond1 and cond2:
                return False
            if cond1 and not cond2:
                g[pos[0]][pos[1]] = '#'
    return g

def find_start(g):
    for i in range(4):
        for j in range(4):
            if g[i][j] == '.':
                return [i, j]

G0 = [['.'] * 4 for _ in [0] * 4]
GX = [['#'] * 4 for _ in [0] * 4]
for i in range(1 << 6):
    used_ps = []
    for j in range(3):
        used_ps.append((j, (i >> 2 * j) & 3))
    for perm_ps in permutations(used_ps):
        p1 = Polyominos[perm_ps[0][0]][perm_ps[0][1]]
        G1 = place_polyomino(0, 0, p1, deepcopy(G0))
        if G1 is False:
            continue
        p2_start = find_start(G1)
        p2 = Polyominos[perm_ps[1][0]][perm_ps[1][1]]
        G2 = place_polyomino(*p2_start, p2, deepcopy(G1))
        if G2 is False:
            continue
        p3_start = find_start(G2)
        p3 = Polyominos[perm_ps[2][0]][perm_ps[2][1]]
        G3 = place_polyomino(*p3_start, p3, deepcopy(G2))
        if G3 == GX:
            print('Yes')
            exit()

print('No')
