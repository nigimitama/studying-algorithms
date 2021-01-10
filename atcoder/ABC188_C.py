N = int(input())
A = list(map(int, input().split()))
idx = list(range(len(A)))
C = A
for i in range(1, N+1):
    wins = []
    for j in range(1, 2**(N-i)+1):
        l1, l2 = [(2*j-1)-1, (2*j)-1]
        win = C[l1] if C[l1] > C[l2] else C[l2]
        wins.append(win)
    C = wins
    if len(C) == 2:
        last = C
winner = C
ans = list(set(last) - set(winner))[0]
print(A.index(ans) + 1)
# 13 AC, 2 RE