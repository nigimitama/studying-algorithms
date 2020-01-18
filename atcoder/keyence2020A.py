h = int(input())
w = int(input())
n = int(input())

x = max(h, w)
a, b = divmod(n, x)
b = 0 if b == 0 else 1
print(a + b)
