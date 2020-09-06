N = int(input())
vp = [list(map(int, input().split())) for _ in range(N)]


def calc_point(v, p):
    if v == 0:
        point = (p // 100) * 5
    if v == 1:
        point = (p // 100) * 3
    if v == 2:
        point = (p // 100) * 2
    if v == 3:
        point = (p // 100) * 1
    return point


prices = {v: p for v, p in [[0, 0], [1, 0], [2, 0], [3, 0]]}
for v, p in vp:
    prices[v] += p


point = 0
for v, p in prices.items():
    point += calc_point(v, p)
print(point)
