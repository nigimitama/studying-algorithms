N, Y = list(map(int, input().split()))

f = False 
for i in range(N+1):
    if f: break
    for j in range(N+1-i):
        l = N - i - j
        s = 10000*i + 5000*j + 1000*l
        if (Y == s) and (l >= 0):
            f = True
            print(i, j, l)
            break
if not f:
    print('-1 -1 -1')
                