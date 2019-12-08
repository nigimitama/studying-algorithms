a, b = list(map(int, input().split()))
n = int([input() for _ in range(1)][0])
c = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if a > c[i][0]:
        ans = "High"
    elif a < c[i][0]:
        ans = "Low"
    else:
        if b > c[i][1]:
            ans = "Low"
        else:
            ans = "High"
    print(ans)
