N,A,B = list(map(int,input().split()))
array = []
for n in range(1,N+1):
    S = sum([int(x) for x in str(n)])
    if A <= S and S <= B:
        array.append(n)
print(sum(array))