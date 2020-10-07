n, s, p = map(int, input().split())
i = p
pages = list(range(1, n+1))[(i-1)*s:min(i*s, n)]
if len(pages) == 0:
    print("none")
else:
    print(" ".join(map(str, pages)))
