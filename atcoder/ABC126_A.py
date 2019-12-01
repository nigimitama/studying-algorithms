N,K = list(map(int,input().split()))
S = [input() for i in range(1)][0]
S = list(S)
S[K-1] = S[K-1].lower()
print("".join(S))
