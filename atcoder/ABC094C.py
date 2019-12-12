N = int(input())
X = list(map(int, input().split()))


def median(a: list):
    l = len(a)
    i = l/2 if (l % 2 == 0) else (l+1)/2
    return sorted(a)[int(i)-1]


for i in range(N):
    X_temp = X[:i] + X[i+1:]
    print(median(X_temp))
