N, M, K = map(int, input().split())
C = list(map(float, input().split()))
X = [list(map(int, input().split())) for _ in range(M)]

scores = []
for i in range(M):
    score = [C[j]*X[i][j] for j in range(N)]
    scores.append(round(sum(score)))

scores.sort(reverse=True)
for l in range(K):
    print(scores[l])
