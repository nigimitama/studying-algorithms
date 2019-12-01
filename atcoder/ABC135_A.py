A,B = list(map(int,input().split()))
ans = (A-B)/2
K = A - ans
if abs(B - K) == abs(ans):
    print(int(K))
else:
    print("IMPOSSIBLE")