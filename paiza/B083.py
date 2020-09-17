"""
方針
----
1. 交差する点を数え上げる
2. 交差する点から長方形が成り立つものを数え上げる
3. 長方形の面積を算出する


結果
----
- 合格：全ケース通過
- 解答時間： 72分55秒(平均解答時間： 56分36秒)
- スコア： 80点

**レーティングは10下がった**
"""
N = int(input())
coords = [list(map(int, input().split())) for _ in range(N)]

# 1. 交差する点を数え上げる


def is_horizontal(x1, y1, x2, y2):
    x_diff = x1 - x2
    y_diff = y1 - y2
    return (x_diff != 0) and (y_diff == 0)


def cross_point(x1, y1, x2, y2, X1, Y1, X2, Y2):
    is_one_h = is_horizontal(x1, y1, x2, y2)
    is_two_h = is_horizontal(X1, Y1, X2, Y2)
    if is_one_h and not is_two_h:
        # 横棒*縦棒
        is_cross = (Y1 <= y1 <= Y2) and (x1 <= X1 <= x2)
        return is_cross, (X1, y1)
    elif not is_one_h and is_two_h:
        # 縦棒*横棒
        is_cross = (X1 <= x1 <= X2) and (y1 <= Y1 <= y2)
        return is_cross, (x1, Y1)
    else:
        # 並行
        return None, (0, 0)


# ある線が、他のすべての線のいずれかと交わっているか
c_points = []
for x1, y1, x2, y2 in coords:  # ある線
    for X1, Y1, X2, Y2 in coords:  # 他のすべての線
        is_cross, c_point = cross_point(x1, y1, x2, y2, X1, Y1, X2, Y2)
        if is_cross:
            c_points.append(c_point)
c_points = list(set(c_points))
# print("c_points", c_points)


# 2. 交差する点から長方形が成り立つものを数え上げる
# xの座標が等しい2組の点をまとめあげて、その点の組同士のyが等しいもの
x_pairs = []
for i in range(len(c_points)):
    for j in range(len(c_points)):
        x1 = c_points[i][0]
        x2 = c_points[j][0]
        if (i != j) and (x1 == x2):
            x_pairs.append((i, j))
# print("x_pairs", x_pairs)

points = []
for i, j in x_pairs:
    x1, y1 = c_points[i]
    x2, y2 = c_points[j]
    x_set1 = set({x1, x2})
    y_set1 = set({y1, y2})
    for i2, j2 in x_pairs:
        x12, y12 = c_points[i2]
        x22, y22 = c_points[j2]
        x_set2 = set({x12, x22})
        y_set2 = set({y12, y22})
        if (x_set1 != x_set2) and (y_set1 == y_set2):
            point = [(x1, y1), (x2, y2), (x12, y12), (x22, y22)]
            points.append(point)
# print("points", points)

# 3. 長方形の面積を算出する
squares = []
for point in points:
    x1, y1 = point[0]
    x2, y2 = point[1]
    x3, y3 = point[2]
    x4, y4 = point[3]
    x_len = abs(x1 - x3)
    y_len = abs(y1 - y2)
    square = x_len * y_len
    squares.append(square)

# print("squares", squares)
print(min(squares))
