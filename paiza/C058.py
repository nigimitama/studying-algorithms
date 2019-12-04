N, t, s  = input().split()
N = int(N)

if s == t:
    print(0)
else:
    for i in range(N):
        s = s[1:] + s[0]
        if s == t:
            count_r = i+1
            break

    for i in range(N):
        s = s[-1] + s[0:(N-1)]
        if s == t:
            count_l = i+1
            break

    print(min(count_r, count_l))
