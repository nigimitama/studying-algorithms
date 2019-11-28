ATK, DEF, AGI = list(map(int, input().split()))
N = int([input() for i in range(1)][0])
lines = [input() for i in range(N)]
S = [line.split() for line in lines]

candidates = []
for s in S:
    if (int(s[1]) <= ATK <= int(s[2])) and (int(s[3]) <= DEF <= int(s[4])) and (int(s[5]) <= AGI <= int(s[6])):
        candidates.append(s[0])

if len(candidates) == 0:
    print("no evolution")
else:
    for candidate in candidates:
        print(candidate)
