h, w, x = map(int, input().split())
s = [input() for _ in range(h)]
s = "".join(s)

indices = [(i, i+x) for i in range(0, len(s), x)]
for start, end in indices:
    print(s[start:end])
