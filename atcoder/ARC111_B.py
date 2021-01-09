# https://atcoder.jp/contests/arc111/tasks/arc111_b
# 制約充足問題?
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]


x = set()
for i in range(N):
    a, b = ab[i]
    if a not in x:
        x.add(a)
    elif b not in x:
        x.add(b)
# print(x)
print(len(x))

# バックトラックを実装しないとこれには対処できない
# 4
# 2 4
# 3 1
# 2 2
# 1 1
