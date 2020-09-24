M = int(input())
N = int(input())
xyc = [list(map(int, input().split())) for _ in range(N)]


def sum_c_group_by_x(xyc):
    res = {}
    for x, y, c in xyc:
        if x not in res:
            res[x] = c
        else:
            res[x] += c
    return res


if __name__ == "__main__":
    sumc: dict = sum_c_group_by_x(xyc)
    n_go = 0
    for c in sumc.values():
        n_go += c // M
        amari = c % M
        if amari != 0:
            n_go += 1
    print(n_go)
