N, K = map(int, input().split())
A = list(map(int, input().split()))

# https://atcoder.jp/contests/abc101/submissions/9269270
print(((N-2) // (K-1))+1)

# WA
# if N == K:
#     y = 0
# else:
#     minA = min(A)
#     count_minA = sum([x == minA for x in A])

#     n_target = N - count_minA
#     n_1 = n_target // (K - 1)
#     n_2 = n_target % (K - 1)
#     y = n_1 + n_2
# print(y)
