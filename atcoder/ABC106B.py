n = int(input())

div8 = []
for i in range(1, n+1, 2):
    count = 0
    for j in range(1, n+1):
        if (i % j) == 0:
            count += 1
    if count == 8:
        div8.append(i)

print(len(div8))