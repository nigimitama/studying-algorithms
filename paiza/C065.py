N = int(input())
ox = [input().split() for _ in range(N)]

n_multiple = 1
for o,x in ox:
    if o == '/':
        n_multiple = int(x)

candidates = []
i = 0
while i <= 150:
    n = n_multiple * i
    is_valid = True
    for o, x in ox:
        if o == '>':
            is_valid &= (n > int(x))
        if o == '<':
            is_valid &= (n < int(x))
        if o == '/':
            is_valid &= (n % int(x) == 0)
    if is_valid:
        candidates.append(n)
    i += 1

print(candidates[0])