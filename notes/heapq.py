# from heapq import *
import heapq

A = [2, 4, 6]

# h = []
# for e in A:
#     heapq.heappush(h, e)
# print(h)

heapq.heapify(A)
heapq.heappush(A, 5)
print(A)



