a, b, x = list(map(int, input().split()))
if a <= x:
    if (a+b) >= x:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
