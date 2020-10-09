t = list(map(int, input().split()))
S = input()

alphabet = [chr(i) for i in range(97, 97+26)]
d = dict(zip(alphabet, t))

out_s = ""
for s in S:
    if d[s] > 0:
        out_s += s
    d[s] -= 1
print(out_s)