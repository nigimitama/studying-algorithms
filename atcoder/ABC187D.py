N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

n_peoples = [(a + b) for a,b in AB]
n_poeples_idx = sorted(range(len(n_peoples)), key=lambda k: n_peoples[k])
n_poeples_idx = n_poeples_idx[::-1]

n_a = sum([ab[0] for ab in AB])
n_b = 0
count = 0
for i in n_poeples_idx:
    if n_a < n_b:
        break
    else:
        n_a -= AB[i][0]
        n_b += n_peoples[i]
        count += 1
    # print(n_a, n_b)
print(count)
# 1部WA/Timeout