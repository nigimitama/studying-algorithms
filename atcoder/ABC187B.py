N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]


def slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = (x2 - x1)
    dy = (y2 - y1)
    if dx == 0 or dy == 0:
        slope = 0
    else:
        slope = dy / dx
    return slope

count = 0
for i in range(N):
    for j in range(i+1, N):
        d = slope(xy[i], xy[j])
        # print(i, j, xy[i], xy[j], d)
        if -1 <= d <= 1:
            count += 1
print(count)

