a,b = input().split()

def S(n: str):
    return sum([int(d) for d in n])

print(max([S(x) for x in [a,b]]))
