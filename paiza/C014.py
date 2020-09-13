# 入力例3がおかしい
n, r = map(int, input().split())
hwd = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if r <= min(hwd[i]):
        print(i+1)
