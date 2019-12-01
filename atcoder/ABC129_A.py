P, Q, R = list(map(int, input().split()))
X = [P + Q, P + R, Q + R]
print(min(X))