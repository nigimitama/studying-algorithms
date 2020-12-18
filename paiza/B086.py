H, W = list(map(int, input().split()))
C = [input() for _ in range(H)]


def split_cake(C, split_i, split_j):
    cells = [[],[],[],[]]
    for i in range(0, split_i+1):
        cells[0].append(C[i][:j+1])
        cells[1].append(C[i][j+1:])
    for i in range(split_i+1, H):
        cells[2].append(C[i][:j+1])
        cells[3].append(C[i][j+1:])
    return cells


def count(s: str):
    footprint = len(s)
    n_berry = len([c for c in s if c == '@'])
    return footprint, n_berry


def calc_utilities(cells):
    utilities = []
    for cell in cells:
        flat_cell = ''
        for c in cell:
            flat_cell += c
        footprint, n_berry = count(flat_cell)
        u = utility(footprint, n_berry)
        utilities.append(u)
    return utilities


def utility(footprint, n_berry):
    return footprint + (n_berry)**2


def inequality(utilities: list):
    return max(utilities) - min(utilities)


min_ineq = 10**9
solution = []
for i in range(H):
    for j in range(W):
        cells = split_cake(C, i, j)
        utilities = calc_utilities(cells)
        ineq = inequality(utilities)
        if ineq < min_ineq:
            min_ineq = ineq
            solution = i, j

print(solution[0]+1, solution[1]+1)
