M, N = map(int, input().split())
m = [int(input()) for _ in range(M)]

amaris = [N % x for x in m]
min_amari_idx = [i for i, x in enumerate(amaris) if x == min(amaris)]

max_i = -1
max_n_pack = -1
for i in min_amari_idx:
    n_pack = N // m[i]
    if n_pack > max_n_pack:
        max_n_pack = n_pack
        max_i = i

print(max_i + 1)
