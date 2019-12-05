N = int(input())
s = [list(map(int, input().split())) for i in range(N)]

start = s[0][0]
end = s[-1][1]
high = max([row[2] for row in s])
low = min([row[3] for row in s])

print(" ".join(list(map(str, [start, end, high, low]))))