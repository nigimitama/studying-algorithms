N = int(input())
actions = [input() for _ in range(N)]


counts = {
    "paper": 0,
    "rock": 0,
    "scissors": 0
}
for action in actions:
    for choice in counts.keys():
        if action == choice:
            counts[action] += 1

is_draw = False
has_all = all([v >= 1 for v in counts.values()])
has_one = len([True for v in counts.values() if v == 0]) == 2
if has_all or has_one:
    is_draw = True
    print("draw")

if not is_draw:
    if (counts["rock"] > 0) and (counts["paper"] > 0):
        print("paper")
    elif (counts["rock"] > 0) and (counts["scissors"] > 0):
        print("rock")
    elif (counts["scissors"] > 0) and (counts["paper"] > 0):
        print("scissors")
