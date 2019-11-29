N, X = list(map(int, input().split()))
K = [int(input()) for i in range(N)]

bin_X = str(bin(X))[2:][::-1]

for k in K:
    print(bin_X[k-1])
