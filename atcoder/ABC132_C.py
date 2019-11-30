# N = 6
# d = list(map(int, "9 1 4 4 6 7".split()))

N = int(input())
input_line = [input() for i in range(1)]
d = list(map(int,input_line[0].split()))
d.sort()
half = int(len(d) / 2)
K = list(range(d[half-1]+1, d[half]+1))
# print(f"K:{K}")
print(len(K))
