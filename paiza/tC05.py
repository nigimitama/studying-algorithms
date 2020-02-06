# https://paiza.jp/works/mondai/skillcheck_archive/umpire?language_uid=python3
n = int(input())
X = [input() for _ in range(n)]

b = 0
s = 0
for x in X:
    if x == "ball":
        b += 1
        if b < 4:
            print("ball!")
        elif b == 4:
            print("fourball!")
            b = 0
    if x == "strike":
        s += 1
        if s < 3:
            print("strike!")
        elif s == 3:
            print("out!")
            s = 0
