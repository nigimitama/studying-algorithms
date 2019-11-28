first_line = input().split()
N = int(first_line[0])
M = int(first_line[1])

# no data error
if N == 0 | M == 0:
    print(0)
else:
    inputs = [input() for i in range(M)]
    P = []
    for i in range(M):
        e_i = inputs[i].split()
        e_i = [int(j) for j in e_i]
        sum_e = sum(e_i)
        if sum_e >= 0:
            P.append(sum_e)
    print(sum(P))