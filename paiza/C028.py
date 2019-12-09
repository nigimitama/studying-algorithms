N = int(input())
qa = [input().split() for _ in range(N)]

total_point = 0
for i in range(N):
    q = qa[i][0]
    a = qa[i][1]
    if q == a:
        point = 2
    elif len(q) == len(a):
        not_eq = []
        for j in range(len(q)):
            not_eq.append(q[j] != a[j])
        
        if sum(not_eq) == 1:
            point = 1
        elif sum(not_eq) >= 2:
            point = 0
    else:
        point = 0
    total_point += point
print(total_point)