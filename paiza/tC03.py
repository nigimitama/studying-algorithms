# https://paiza.jp/works/mondai/skillcheck_archive/search_history?language_uid=python3
n = int(input())
w = [input() for _ in range(n)]
w = w[::-1]

s = []
for v in w:
    if v not in s:
        s.append(v)
        print(v)

