A = int(input())
B,C,X = [int(input()) for i in range(3)]

count = 0
for i in range(A+1):
    for j in range(B+1):
        for l in range(C+1):
            Y = 500*i + 100*j + 50*l
            if X == Y:
                count += 1
print(count)