N, X = list(map(int, input().split()))
input_line = [input() for i in range(1)]
L = list(map(int, input_line[0].split()))

D = []
for i in range(N+1):
    if i == 0:
        D += [0]
    else:
        D += [D[i-1] + L[i-1]]

# print(f"D:{D}")

counter = 0
for i in range(N+1):
    if D[i] <= X:
        counter += 1

print(counter)
    # if D[i] == X:
    #     print(i+1)
    #     exit(0)
    # elif D[i] >= X:        
    #     print(i)
    #     exit(0)


