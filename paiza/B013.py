a, b, c = map(int, input().split())
n = int(input())
hm = [list(map(int, input().split())) for _ in range(n)]


def to_hour(h, m):
    return h + m / 60


def to_str(h):
    hour = int(h // 1)
    minute = round(h % 1 * 60)
    return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}"


limit = to_hour(h=8, m=59)
ride_limit = limit - to_hour(h=0, m=c) - to_hour(h=0, m=b)
arrives = [to_hour(h, m) for h, m in hm]
ride = max([arrive for arrive in arrives if arrive < ride_limit])
wakeup = ride - to_hour(h=0, m=a)
print(to_str(wakeup))
