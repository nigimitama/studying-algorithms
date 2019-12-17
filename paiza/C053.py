N = int(input())
c = input().split()
tentimes = True if "x10" in c else False
c = [int(x) for x in c if x != "x10"]
s = sum(c)
if min(c) == 0:
    s -= max(c)
if tentimes:
    s *= 10
print(s)
