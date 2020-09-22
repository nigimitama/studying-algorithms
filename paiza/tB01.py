# https://paiza.jp/works/mondai/skillcheck_sample/long-table?language_uid=python3


def get_index(i_start, delta, table):
    indices = []
    for i in range(i_start, i_start + delta):
        if i >= len(table):
            i = i - len(table)
        indices.append(i)
    return indices


n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

table = [0]*n
n_customers = 0
for a, b in ab:
    i_start = b - 1

    indices = get_index(i_start, a, table)
    is_empty = sum([table[i] for i in indices]) == 0

    if is_empty:
        n_customers += a
        for i in indices:
            table[i] = 1

print(n_customers)
