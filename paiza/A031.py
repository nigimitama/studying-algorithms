P1,P2,P3,k = list(map(int, input().split()))
max_e = 40
a = []
for i in range(max_e):
    for j in range(max_e):
        for l in range(max_e):
            a.append(1 * P1**i * P2**j * P3**l)
a.sort()
print(a[k-1])