S = input()
X = 0
for i in range(len(S)):
    if S[i] == "+":
        X += 1
    else:
        X -= 1

print(X)