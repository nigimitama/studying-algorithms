# this is failed
L = int(input())
u, a, b = list(map(int, input().split()))
v = int(input())

def usagi_runtime(L, u, a, b):
    kpm = 1 / u
    km = 0
    minute = 0
    while L > km:
        if (km > 0) & (km % a == 0):
            minute += b
        km += kpm
        minute += 1
    return minute

u_time = usagi_runtime(L, u, a, b)
k_time = L * v

if u_time > k_time:
    print("KAME")
elif u_time < k_time:
    print("USAGI")
else:
    print("DRAW")
