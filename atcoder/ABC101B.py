n = int(input())
s = str(n)
s = sum([int(s[i]) for i in range(len(s))])
if n % s == 0:
    print("Yes")
else:
    print("No")
