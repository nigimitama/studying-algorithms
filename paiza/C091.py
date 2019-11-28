N = int(input())
S = [input() for x in range(N)]
# init
x1 = 0
x2 = 0

for i in range(N):
    order = S[i].split()
    if order[0] == 'SET':
        if order[1] == '1':
            x1 = int(order[2])
        if order[1] == '2':
            x2 = int(order[2])
    if order[0] == 'ADD':
        x2 = x1 + int(order[1])
    if order[0] == 'SUB':
        x2 = x1 - int(order[1])
print(x1, x2)