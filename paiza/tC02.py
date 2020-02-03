from collections import OrderedDict
s = input().split()
count = OrderedDict()

# init
for s_i in s:
    count[s_i] = 0

# count
for s_i in s:
    count[s_i] += 1

for k, v in count.items():
    print(k, v)
