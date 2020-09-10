# 一部のテストケースでfailed.でも原因わからなかった
price, a, b = map(int, input().split())
by = None
while True:
    if (price + 10) <= a:
        price += 10
        by = "A"
    if (price + 1000) <= b:
        price += 1000
        by = "B"
    if ((price + 10) > a) or ((price + 1000) > b):
        break

print(by, price)
