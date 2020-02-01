m, n, k = map(int, input().split())
a = [int(input()) for _ in range(k)]

# num of supporters
s = [0 for _ in range(m+1)]
s[0] = n  # no supporter

for i in range(k):
    candidate = a[i]
    for j in range(len(s)):
        if (s[j] > 0) and (j != candidate):
            s[j] -= 1
            s[candidate] += 1

del s[0]
max_s = max(s)
for i in range(len(s)):
    if s[i] == max_s:
        print(i+1)
