N = int(input())
ch = [input().split() for _ in range(N)]

min_le = 10**9
max_ge = 0
for c, h in ch:
    h = float(h)
    if c == "le" and h < min_le:
        min_le = h
    if c == "ge" and h > max_ge:
        max_ge = h
print(max_ge, min_le)
