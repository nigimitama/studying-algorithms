N, X = list(map(int, input().split()))
m = [int(input()) for _ in range(N)]
# make all
X = X - sum(m)
count = N
# make remain
count += X // min(m)
print(count)