N, M = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(1)][0]
A = [-1*x for x in A]

import heapq
heapq.heapify(A)

while M != 0:
    x = heapq.heappop(A)
    y = -x // 2
    heapq.heappush(A, -y)
    M -= 1

A = [-1*x for x in A]
print(sum(A))
