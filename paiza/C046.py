n = int(input())
s = input().split()
m = int(input())
op = [input().split() for _ in range(m)]

members = dict(zip(s, [0]*n))
for o,p in op:
    members[o] += int(p)

names = list(members.keys())
prices = list(members.values())
idx = sorted(range(len(prices)), key=lambda k: prices[k], reverse=True)
for i in idx:
    print(names[i])
