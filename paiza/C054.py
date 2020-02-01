n,v = map(int, input().split())
tp =  [list(map(int, input().split())) for _ in range(n)]

is_out = False
for i in range(n):
    for j in range(i+1, n):
        dp = tp[j][1] - tp[i][1]
        dt = tp[j][0] - tp[i][0]
        s = dp / dt
        if s > v:
            is_out = True

if is_out:
    print("YES")
else:
    print("NO")
