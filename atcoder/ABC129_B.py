N = int(input())
input_line = [input() for i in range(1)]
W = list(map(int, input_line[0].split()))

D = []
for T in range(1,N):
    S1 = sum(W[:T])
    S2 = sum(W[T:])
    D.append(abs(S1 - S2))
print(min(D))


