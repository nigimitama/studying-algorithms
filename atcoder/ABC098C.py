s = input()
k = int(input())
# TLE
chars = list(s)
for w in range(2, len(s)+1):
    chars += [s[i:i+w] for i in range(len(s))]
chars = list(set(chars))
chars.sort()
print(chars[k-1])