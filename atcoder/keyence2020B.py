n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
x = [xl_i[0] for xl_i in xl]
x_idx = sorted(range(len(x)), key=lambda k: x[k])
xl = [xl[i] for i in x_idx]

j = 1
m = len(xl)
while j < m:
    x_i, l_i = xl[j-1]
    x_j, l_j = xl[j]
    if (x_i + l_i) > (x_j - l_j):
        xl.remove(xl[j])
        j = 0
    j += 1
    m = len(xl)

print(len(xl))
