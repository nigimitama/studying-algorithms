N = int(input())
f = [int(input()) for i in range(N)]

log = []
for i in range(N):
    if i == 0:
        move = f[i] - 1
    else:
        move = abs(f[i] - f[i-1])
    log.append(move)
print(sum(log))