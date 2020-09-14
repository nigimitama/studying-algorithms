T, x, y = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(T)]

is_alive = True
max_x = x
for a,b in ab:
    x += a
    y += b
    if x > max_x and is_alive:
        max_x = x
    if y <= 0 and is_alive:
        is_alive = False
print(max_x)