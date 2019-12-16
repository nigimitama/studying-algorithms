p1, p2 = list(map(int, input().split()))
p3, p4 = list(map(int, input().split()))
e = list(map(int, input().split()))
f = list(map(int, input().split()))


win11 = p1 if (e[p1-1] < e[p2-1]) else p2
win12 = p3 if (e[p3-1] < e[p4-1]) else p4
wix = sorted([win11, win12])
if (f[0] < f[1]):
    win2 = wix[0] 
    lose2 = wix[1]
else: 
    win2 = wix[1] 
    lose2 = wix[0]

print(win2)
print(lose2)


