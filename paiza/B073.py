N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
Q = int(input())
SE = [list(map(int, input().split())) for _ in range(Q)]

for s, e in SE:
    s -= 1
    mean_A = sum(A[s:e]) // len(A[s:e])
    lack = M - mean_A
    if lack > 0:
        for i in range(s, e):
            A[i] += lack
        
print(' '.join(map(str, A)))
# 一部ケースでWA