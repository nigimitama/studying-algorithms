X, Y, Z = map(int, input().split())
N = int(input())
st = [list(map(int, input().split())) for _ in range(N)]

income = 0
for s, t in st:
    for h in range(s, t):
        if (9 <= h) & (h < 17):
            income += X
        elif (17 <= h) & (h < 22):
            income += Y
        else:
            income += Z
print(income)