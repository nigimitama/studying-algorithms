xc, yc, r1, r2 = map(int, input().split())
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]


def is_in(x, y):
    if r1**2 <= ((x - xc)**2 + (y - yc)**2) <= r2**2:
        print("yes")
    else:
        print("no")


for x, y in xy:
    is_in(x, y)
