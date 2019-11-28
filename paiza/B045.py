import random
# input
MN = input().split()
M = int(MN[0])
N = int(MN[1])

for i in range(M):
    n1 = int(random.uniform(45, 0))
    n2 = int(random.uniform(44, 0))
    print(f"{n1} + {n2} =")

for i in range(N):
    n1 = int(random.uniform(99, 0))
    n2 = int(random.uniform(99, 0))
    print(f"{n1} - {n2} =")
