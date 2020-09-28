N, M = map(int, input().split())
cards = [int(input()) for _ in range(N)]

counts = {}
i = 1
for card in cards:
    if card not in counts:
        counts[card] = 1
    else:
        counts[card] += 1
    if len(counts) == M:
        break
    else:
        i += 1

if len(counts) == M:
    print(i)
else:
    print('unlucky')
