N, Y = map(int, input().split())
M = int(input())
a = list(map(int, input().split()))

correct = 0
wrong = 0
button = 1
for i in range(M):
    if a[i] == button:
        correct += 1
    else:
        wrong += 1
    button += 1
    if button > N:
        button = 1

if wrong < Y:
    score = correct*1000
else:
    score = -1
print(score)
