N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
x = 0
for a, b in zip(A, B):
    x += (a * b)

if x == 0:
    print('Yes')
else:
    print('No')
