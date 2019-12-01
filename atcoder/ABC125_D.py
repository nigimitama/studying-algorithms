inputs = [input() for i in range(2)]
N = int(inputs[0])
A = inputs[1].split()
A = [int(i) for i in A]



N=5
A = "10 -4 -8 -11 3".split()
A = [int(i) for i in A]
i=1
for i in range(N-1):
    print(i)
    before = A[i] + A[i+1]
    after = A[i]*-1 + A[i+1]*-1
    if before < after:
        # 次の次に譲るか
        if (i+3) < N:
            next2 = A[i+2] + A[i+3]
            next2_do = A[i+2]*-1 + A[i+3]*-1
            if next2 < next2_do:
                # 次に譲るか
                if (i+2) < N:
                    now_do = after + A[i+2]
                    next_do = A[i] + A[i+1]*-1 + A[i+2]*-1 # 次回に譲るパターン
                    if now_do > next_do:
                        A[i] = A[i] * -1
                        A[i+1] = A[i+1] * -1
                else:
                    A[i] = A[i] * -1
                    A[i+1] = A[i+1] * -1
    print(A)

print(sum(A))