a = list(map(int, input().split()))
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    c = 0
    for j in range(6):
        for a_i in a:
            if a_i == d[i][j]:
                c += 1
    print(c)
