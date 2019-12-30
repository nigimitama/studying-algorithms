N = int(input())
M = int(N*(N-1)/2)
r = [list(map(int, input().split())) for _ in range(M)]

# 2次元配列の初期化はリスト内包表記を使わないと（*Nで済ますと）
# 参照わたしになってしまう
t = [list("-"*N) for _ in range(N)]
for f, s in r:
    t[f-1][s-1] = "W"
    t[s-1][f-1] = "L"

for t_i in t:
    print(" ".join(t_i))