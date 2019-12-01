N = int(input())
input_line = [input() for i in range(1)]
A = list(map(int,input_line[0].split()))

count = 0
while True:
    ans = []
    for i in range(N):
        ans.append(A[i] % 2 == 0)
    if all(ans):
        count += 1
        A = [int(x / 2) for x in A]
    else:
        break
print(count)