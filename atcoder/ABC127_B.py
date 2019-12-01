r, D, x_2000 = list(map(int, input().split()))
# input_line = [input() for i in range(H)]

x = []
for i in range(0,10):
    if i == 0:
        x.append(r * x_2000 - D)
        print(x[i])
    else:
        x.append(r * x[i-1] - D)
        print(x[i])
