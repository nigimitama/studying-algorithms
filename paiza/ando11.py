# https://paiza.jp/poh/ando/challenge/59149986/ando11
n = int(input())
img1 = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
img2 = [list(map(int, input().split())) for _ in range(m)]

for i in range(0, (n-m)+1):
    for j in range(0, (n-m)+1):
        rows = img1[i:i+m]
        rows = [row[j:j+m] for row in rows]
        if rows == img2:
            print(i, j)
