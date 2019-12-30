a, b = map(int, input().split())


def cumsum(n):
    return int(n*(n+1) / 2)


delta_h = b - a
h_2 = cumsum(delta_h)
print(h_2 - b)
