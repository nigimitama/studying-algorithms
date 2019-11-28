first_line = input().split()
N = int(first_line[0])
M = int(first_line[1])
inputs = [input() for i in range(N)]

for i in range(N):
    a, b = inputs[i].split()
    a = int(a)
    b = int(b)
    # penalty
    score = a - (b * 5)
    # no-minus
    if score < 0:
        score = 0
    # is over border
    if score >= M:
        print(i+1)
