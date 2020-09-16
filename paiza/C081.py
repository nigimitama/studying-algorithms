N = int(input())
td = [input().split() for _ in range(N)]

data = {}
for t, d in td:
    if t not in data:
        data[t] = {"L": 0, "R": 0}
    data[t][d] += 1

pair = 0
for value in data.values():
    pair += min(list(value.values()))

print(pair)
