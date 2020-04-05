k, n = map(int, input().split())
da = [list(map(int, input().split())) for _ in range(k)]

def evaluate(a):
    if a >= 80:
        print("A")
    elif (70 <= a) and (a <= 79):
        print("B")
    elif (60 <= a) and (a <= 69):
        print("C")
    else:
        print("D")


point_per_problem = int(100 / n)
for d, a in da:
    # 点数計算
    p = a * point_per_problem
    # 遅れに応じた補正
    if (1 <= d) and (d <= 9):
        p = int(p * 0.8)
    elif d >= 10:
        p = 0
    evaluate(p)
