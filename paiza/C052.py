H, W = map(int, input().split())
dy, dx = map(int, input().split())

dy, dx = abs(dy), abs(dx)
o = (H * dx) + (W * dy) - (dy * dx)
print(o)
