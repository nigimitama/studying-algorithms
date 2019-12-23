N = int(input())
dp = [list(map(int, input().split())) for _ in range(N)]

import math
point = 0
for d, p in dp:
    d = str(d)
    if "3" in d:
        point += math.floor(p*0.03)
    elif "5" in d:
        point += math.floor(p*0.05)
    else:
        point += math.floor(p*0.01)
print(point)
        
