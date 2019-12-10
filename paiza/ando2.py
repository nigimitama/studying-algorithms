n = int(input())
t = [int(input()) for _ in range(n)]

wakeup = 7*60
base = 6*60

def showtime(x: int):
    if x < 0:
        x = 24*60 + x
    h, m = divmod(int(x), 60)
    return str(h).zfill(2)+":"+str(m).zfill(2)

for i in range(len(t)):
    print(showtime(wakeup - base - t[i]/3))


# https://paiza.jp/poh/ando/mypage/59149986?c=7a8ee24c