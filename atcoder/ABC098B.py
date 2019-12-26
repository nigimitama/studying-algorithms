N = int(input())
S = input()

max_c = 0
for i in range(N):
    a = S[0:i]
    b = S[i:]
    c = len(set(a) & set(b))
    if c > max_c:
        max_c = c
print(max_c)
