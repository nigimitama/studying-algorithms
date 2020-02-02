# https://paiza.jp/works/mondai/skillcheck_sample/long-table?language_uid=python3
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]

table = [0]*n

for a, b in ab:
    b = b - 1
    if sum(table[b:b+a]) == 0:
        table[b:b+a] = [1]*a

print(sum(table))
