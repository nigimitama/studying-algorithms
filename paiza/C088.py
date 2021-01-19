N = int(input())
prices = list(map(int, input().split()))
money, Q = list(map(int, input().split()))
xk = [list(map(int, input().split())) for _ in range(Q)]

for item, size in xk:
    pay = prices[item-1] * size
    if money >= pay:
        money = money - pay
print(money)
