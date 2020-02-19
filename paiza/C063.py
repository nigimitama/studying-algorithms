n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

bloom_days = []
for a, b in ab:
    bloom_days.append(b+a)

n_bloom_days = {}
for i in set(bloom_days):
    n_bloom_days[i] = 0

for i in bloom_days:
    n_bloom_days[i] += 1

max_v = 0
for key in set(bloom_days):
    v = n_bloom_days[key]
    if v > max_v:
        max_v = v
        max_k = key
print(max_k)