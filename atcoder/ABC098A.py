A,B = map(int, input().split())
max_v = -10**9
tmp = A + B
max_v = tmp if max_v < tmp else max_v
tmp = A - B
max_v = tmp if max_v < tmp else max_v
tmp = A * B
max_v = tmp if max_v < tmp else max_v
print(max_v)
    