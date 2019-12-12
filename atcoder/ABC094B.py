n, m, x = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(1)][0]

cost1 = 0
for i in range(x, n+1):
    if i in a:
        cost1 += 1
cost2 = 0
for i in range(x):
    i = x-i
    if i in a:
        cost2 += 1
print(min(cost1, cost2))
