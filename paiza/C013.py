n  = (input())
m = int(input())
r = [(input()) for _ in range(m)]

ok = []
for r_i in r:
    if n not in r_i:
        ok.append(r_i)
        print(r_i)

if len(ok) == 0:
    print("none")
    