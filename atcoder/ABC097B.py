X = int(input())
y = 1
for b in range(1, X):
    for p in range(2, X):
        tmp = b**p
        if y < tmp:
            if tmp <= X:
                y = tmp
            else:
                break
print(y)
