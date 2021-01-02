# 1部WA/Timeout
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

"""
解説
https://atcoder.jp/contests/abc187/editorial/486

1. X = (高橋氏の得る票数) − (青木氏の得る票数)とし、X>0になるようにすればよい
2. i番目の町で演説すると高橋がA+Bだけ増えて青木がAだけ減るので、Xは2A+Bだけ増える
3. Xが高い順に演説していけばいい
よって
↓
"""
# 修正後、AC
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
X_gain = [(2*a+b) for a,b in AB]  # その町で演説したら得られるXの増分
X_gain.sort(reverse=True)
X = -sum([a for a,b in AB])   # 初期値（高橋が0、青木が全部）

count = 0
for i in range(N):
    if X > 0:
        break
    else:
        X += X_gain[i]
        count += 1
print(count)