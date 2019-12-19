a, b, R = list(map(int, input().split()))
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    x = xy[i][0]
    y = xy[i][1]
    rad = (x - a)**2 + (y - b)**2
    if R**2 <= rad:
        print("silent")
    else:
        print("noisy")

