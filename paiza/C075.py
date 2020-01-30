n, m = map(int, input().split())
f = [int(input()) for _ in range(m)]

p = 0
for i in range(m):
    if p >= f[i]:
        p -= f[i]
    else:
        n -= f[i]
        p += int(f[i] * 0.1)
    print(n, p)
    