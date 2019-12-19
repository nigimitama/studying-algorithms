N, C = list(map(int, input().split()))
xv = [list(map(int, input().split())) for _ in range(N)]

posision = 0
profit = 0
for x, v in xv:
    cost_r = abs(posision - x)
    cost_l = abs(C - cost_r)
    profit_i = v - min(cost_r,  cost_l)
    if profit_i < 0:
        pass
    else:
        profit += profit_i
        posision = x
    print(profit,profit_i, v, min(cost_r,  cost_l))
print(profit)