E = input()
y = 0
for i in range(len(E)):
    if E[i] == "/":
        y += 1
    if E[i] == "<":
        y += 10
print(y)
