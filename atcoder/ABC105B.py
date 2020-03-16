n = int(input())

can = False
for i in range(26):
    for j in range(15):
        v = (i*4 + j*7)
        if v != 0:
            if n % v == 0:
                can = True
if can:
    print("Yes")
else:
    print("No")
