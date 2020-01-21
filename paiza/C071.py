m,n = map(int, input().split())

c = 0
for j in range(1, m):
    for i in range(1, n):
        y = (i**2 + j**2)**(1/2)
        if int(y) == y:
            c += 1
print(c)
