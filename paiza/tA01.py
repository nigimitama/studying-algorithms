# https://paiza.jp/works/mondai/skillcheck_sample/janken?language_uid=python3
n, m = map(int, input().split())
s = input()

n = 6
m = 25
s = "PCGCPC"

count = {"G": 0, "C": 0, "P": 0}
for i in range(len(s)):
    for k in count.keys():
        if s[i] == k:
            count[k] += 1

for _ in range(count["G"]):
    if m > 5:
        m += 5

# 全然わからん！


class Janken:

    def __init__(self, m):
        self.m = m
        self.t = 0

    def goo(self, s):
        self.m -= 0
        if s == "C":
            self.t += 1

    def choki(self, s):
        self.m -= 2
        if s == "P":
            self.t += 1

    def paa(self, s):
        self.m -= 5
        if s == "G":
            self.t += 1


j = Janken(m)
for i in range(len(s)):
    # もしちょうどの値なら相手に関わらず手を出す
    if j.m == 5:
        j.paa(s[i])
    elif j.m == 2:
        j.choki(s[i])
    # それ以外なら選んで手を出す
    elif s[i] == "G" and j.m >= 5:
        j.paa(s[i])
    elif s[i] == "P" and j.m >= 2:
        j.choki(s[i])
    else:
        j.goo(s[i])
print(j.t)
