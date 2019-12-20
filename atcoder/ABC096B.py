N = list(map(int, input().split()))
K = int(input())

max_N = max(N)
y = sum(N) - max_N + max_N*2**K
print(y)
