N, S, p = map(int, input().split())
ms = [list(map(int, input().split())) for _ in range(N)]

max_m = 0
max_m_index = 0
for i in range(N):
    index = i+1
    m, s = ms[i]
    if ((S-p) <= s) and (s <= (S+p)):
        if m > max_m:
            max_m = m
            max_m_index = index

if max_m == 0:
    print("not found")        
else:
    print(max_m_index)
