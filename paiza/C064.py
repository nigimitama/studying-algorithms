M, N = list(map(int, input().split()))
lines = [input() for _ in range(M+N)]
c = list(map(int, lines[0:M]))
a = [list(map(int, al.split())) for al in lines[M:]]

c = [c_i / 100 for c_i in c]

for a_i in a:
    ca_i = 0
    for j in range(M):
        ca_i += int(a_i[j] * c[j])
    print(ca_i)