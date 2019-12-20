# WA
# see https://atcoder.jp/contests/abc096/submissions/9020918
H, W = list(map(int, input().split()))
c = [list(input()) for _ in range(H)]


def ix(index, H=H, W=W):
    if index < 0:
        index = 0
    if index >= H:
        index = (H-1)
    if index >= W:
        index = (W-1)
    return index


for i in range(H):
    for j in range(W):
        if c[i][j] == "#":
            result = "No"
            if (ix(i - 1) != i) and (c[ix(i-1)][j] == "#"):
                result = "Yes"
            if (ix(i + 1) != H-1) and (c[ix(i+1)][j] == "#"):
                result = "Yes"
            if (ix(j - 1) != j) and (c[i][ix(j-1)] == "#"):
                result = "Yes"
            if (ix(j + 1) != W-1) and (c[i][ix(j+1)] == "#"):
                result = "Yes"
            if result == "No":
                break
print(result)
