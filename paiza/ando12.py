x, y, z, n = list(map(int, input().split()))
da = [list(map(int, input().split())) for _ in range(n)]

volumes = []
for i in range(n):
    if i == 0:
        d = x if (da[i][0] == 0) else da[i][0]
        a = y if (da[i][1] == 0) else da[i][1]
    else:
        if (da[i][0] == 0):
            d = x
        elif abs(da[i-1][0] - da[i][0]) == 0:
            d = da[i][0]
        else:
            d = abs(da[i-1][0] - da[i][0])
        
        if (da[i][1] == 0):
            a = y
        elif abs(da[i-1][1] - da[i][1]) == 0:
            a = da[i][1]
        else:
            a = abs(da[i-1][1] - da[i][1])
    v = d * a * z
    volumes.append(v)
    print(i, v, d, a)
d = (x - da[i][0])
a = (y - da[i][1])
v = d * a * z
volumes.append(v)
print(i, v, d, a)
print(min(volumes))