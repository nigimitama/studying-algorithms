y, m, d = map(int, input().split())
a, b = map(int, input().split())


def daydiff(y1, m1, d1, y2, m2, d2):
    y, m, d = y1, m1, d1
    n_days = 0
    while y <= y2:
        while m <= 13:
            while d <= _days(m):
                if (y == y2) and (m == m2) and (d == d2):
                    return n_days
                else:
                    n_days += 1
                    d += 1
            m += 1
            d = 1
        y += 1
        m = 1
    return n_days


def _days(m):
    if m % 2 == 0:
        return 15
    else:
        return 13


is_fes = False
yp = y
while is_fes == False:
    yp += 1
    if yp % 4 == 1:
        is_fes = True
        ds = daydiff(y, m, d, yp, a, b)

print(ds)
