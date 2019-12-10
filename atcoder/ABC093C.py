x = list(map(int, input().split()))
m = max(x)
d = [v - m for v in x]
count = 0
while sum(d) != 0:
    ix = [i for i in range(len(x)) if x[i] != m]
    if len(ix) == 2:
        x[ix[0]] += 1
        x[ix[1]] += 1
    if len(ix) == 1:
        x[ix[0]] += 2
    m = max(x)
    d = [v - m for v in x]
    count += 1
print(count)
