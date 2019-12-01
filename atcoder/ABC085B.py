N = int(input())
d = [input() for i in range(N)]
d = list(set(d))
print(len(d))