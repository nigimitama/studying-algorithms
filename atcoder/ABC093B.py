A, B, K = list(map(int, input().split()))

if (A+K) < (B-K+1):  
  for x in range(A,A+K):
    print(x)

  for x in range(B-K+1,B+1):
    print(x)
else:
  for x in range(A,B+1):
    print(x)
