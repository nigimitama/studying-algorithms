N = int(input())

data = {}
for i in range(1,N+1):
    data[i] = []

for _ in range(N):
    A = [int(input()) for _ in range(1)][0]
    xy = [list(map(int, input().split())) for _ in range(A)]
    for xy_i in xy:
        data[xy_i[0]].append(xy_i[1])

print(data)
        
# ぜんぜんわからん！