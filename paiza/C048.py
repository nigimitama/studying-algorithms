x, p = list(map(int, input().split()))

y = x
while x > 0:
    x = int(x - x*(p/100))
    y += x

print(y)

