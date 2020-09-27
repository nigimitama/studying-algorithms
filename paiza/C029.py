M, N = map(int, input().split())
dr = [list(map(int, input().split())) for _ in range(M)]

min_mean_r = 100
min_dates = None
for i in range(M):
    dr_i = dr[i:i+N]
    if len(dr_i) == N:
        r = [r for d, r in dr_i]
        d = [d for d, r in dr_i]

        mean_r = sum(r) / N
        if mean_r < min_mean_r:
            min_mean_r = mean_r
            min_dates = d
print(min_dates[0], min_dates[-1])