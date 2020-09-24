N = int(input())
a = [input() for _ in range(N)]


def plural(s):
    if (s[-1] in {"s", "o", "x"}) or (s[-2:] in {"sh", "ch"}):
        s += "es"
    elif s[-1] == "f":
        s = s.replace("f", "ves")
    elif s[-2:] == "fe":
        s = s.replace("fe", "ves")
    elif s[-1] == "y" and (s[-2] not in {"a", "i", "u", "e", "o"}):
        s = s.replace("y", "ies")
    else:
        s += "s"
    return s


for a_i in a:
    print(plural(a_i))
