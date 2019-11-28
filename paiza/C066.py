M, N, x = list(map(int, input().split()))
W = [int(input()) for x in range(M)]

x_now = x
poi = 1
i = 0
while (poi <= N) and (i < M):
    x_remain = x_now - W[i]
    if x_remain > 0:
        i += 1
        x_now = x_remain
    else:
        poi += 1
        x_now = x
print(i)



