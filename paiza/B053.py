H, W = map(int, input().split())
a0 = list(map(int, input().split()))
a1 = list(map(int, input().split()))
A = [a0, a1]

# make Y
def each_slice(arr, n):
    return [arr[i:i + n] for i in range(0, len(arr), n)]

Y = [0] * W * H
Y = each_slice(Y, W)

# copy
for i in range(2):
    for j in range(2):
        Y[i][j] = A[i][j]

for i in range(H):
    for j in range(W):
        if Y[i][j] == 0:
            if j != 0:
                Y[i][j] = Y[i][(j-1)] + (Y[i][1] - Y[i][0])
            if i != 0:
                Y[i][j] = Y[(i-1)][j] + (Y[1][j] - Y[0][j])


for i in range(H):
    y = str(Y[i]).replace(']', '').replace('[', '').replace(',', '')
    print(y)


# H, W = 5, 7
# a0 = [1,5]
# a1 = [-2,1]


# H, W = 5, 5
# a0 = [1,2]
# a1 = [3,4]
