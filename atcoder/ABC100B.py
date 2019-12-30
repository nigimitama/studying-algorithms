D, N = map(int, input().split())
# WA
if D == 0:
    if N == 100:
        print(1+N)
    else:
        print(N)
else:    
    print(100**D*N)
