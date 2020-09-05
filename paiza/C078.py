N, c1, c2 = map(int, input().split())
p = [int(input()) for _ in range(N)]

n_stock = 0
income = 0
for i in range(N):
    if (i+1) == N:
        income += p[i]*n_stock
        n_stock = 0
    else:
        if (c1 < p[i] < c2):
            pass
        elif p[i] <= c1:
            income -= p[i]
            n_stock += 1
        elif p[i] >= c2:
            income += p[i]*n_stock
            n_stock = 0

print(income)
