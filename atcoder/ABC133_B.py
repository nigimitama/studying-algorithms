import math
N,D = list(map(int,input().split()))
X = [list((map(int,input().split()))) for i in range(N)]

def diff(A,B,D):
    y = []
    for l in range(D):
        y.append((A[l] - B[l])**2)
    return math.sqrt(sum(y))

count = 0
for i in range(N):
    for j in range(i+1,N):
        y = diff(X[i], X[j], D)
        if y % 1 == 0:
            count += 1
print(count)