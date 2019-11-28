q = int(input())
inputs = [input() for i in range(q)]

def is_perfect(N):
    Y = []
    for i in range(1, N-1):
        if N % i == 0:
            Y.append(i)
    S = sum(Y)
    if N == S:
        res = "perfect"
    elif abs(N - S) == 1:
        res = "nearly"
    else:
        res = "neither"
    return res


for n in inputs:
    print(is_perfect(int(n)))
