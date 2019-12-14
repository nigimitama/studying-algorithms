N, K, P = list(map(int, input().split()))
s = input().split()
s.sort()

for word in s[K*(P-1):K*P]:
    print(word)