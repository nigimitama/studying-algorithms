N = int(input())
input_line = [input() for i in range(1)]
p = list(map(int,input_line[0].split()))

counter = 0
for i in range(0,N-2):
    b = p[i:i+3]
    b.sort()
    if b[1] == p[i:i+3][1]:
        counter += 1
print(counter)