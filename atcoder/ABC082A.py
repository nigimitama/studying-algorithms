a,b = list(map(int, input().split()))
import math
x = (a+b) / 2
decimal = x - math.floor(x)
if decimal != 0:
    a = math.floor(x) + 1
else:
    a = math.floor(x)
print(a)

