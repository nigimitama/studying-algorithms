N = int(input())
A = [list(map(int, input().split())) for _ in range(1)][0]

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += A[i] ^ A[j]
print(ans % (10**9 + 7))
