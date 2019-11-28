# method: 運賃計算
# 初乗り距離 a_i、 初乗り運賃 b_i、 加算距離 c_i、 加算運賃 d_i 
def how_fee(X, a, b, c, d): 
    if X < a: # 初乗り距離未満なら初乗り運賃
        fee = b
    else:
        meter = (X - a) // c + 1
        fee = b + meter*d
    return fee


# data1
first_line = input().split()
N = int(first_line[0]) # 台数
X = int(first_line[1]) # 距離
# data2
inputs = [input() for i in range(N)]
fee = []
for i in range(N):
        abcd_i = inputs[i].split()
        abcd_i = [int(j) for j in abcd_i]
        fee_i = how_fee(X, abcd_i[0], abcd_i[1], abcd_i[2], abcd_i[3])
        fee.append(fee_i)
print(min(fee), max(fee))
