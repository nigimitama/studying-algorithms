N = int(input())
S = [input() for _ in range(N)]
S_ = set(S)


def is_dissatisfied(s: str, S_: set):
    return (s in S_) and ('!' + s in S_)


dissatisfied = None
for s in S:
    if is_dissatisfied(s, S_):
        dissatisfied = s
        break

if dissatisfied:
    print(dissatisfied)
else:
    print('satisfiable')
