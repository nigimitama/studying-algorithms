s = input()
n = len(s)
first = s[:int(n/2)]
latter = s[int(n/2):]
latter = latter[::-1]

diff = 0
for i in range(int(n/2)):
    diff += 1 if (first[i] != latter[i]) else 0
print(diff)