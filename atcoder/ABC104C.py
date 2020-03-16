d,g = map(int,input().split())
pc = [list(map(int, input().split())) for _ in range(d)]

max_scores = []
i = 1
for p, c in pc:
    max_i = i*100 * p + c
    max_scores.append(max_i)

# wakaran

