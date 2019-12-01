# WA

# H, W = [7,7]
# s = ['#######', '#X.2..#', '#.#.#.#', '#.X.1.#', '#.#1#.#', '#4....#', '#######']
s = [['#', '#', '#', '#', '#', '#', '#'], ['#', 'X', '.', '2', '.', '.', '#'], ['#', '.', '#', '.', '#', '.', '#'], ['#', '.', 'X', '.', '1', '.', '#'], ['#', '.', '#', '1', '#', '.', '#'], ['#', '4', '.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]

H, W = list(map(int, input().split()))
s = [list(input()) for x in range(H)]
import re

def is_digit(string):
    return re.match(r"\d", s[i][j]) is not None

bombs = []
enemies = []
for i in range(H):
    for j in range(W):
        if is_digit(s[i][j]):
            bomb = [int(s[i][j]), i, j]
            bombs.append(bomb)
        if s[i][j] == "X":
            enemies.append([i, j])


# get bombs
bombs = []
for i in range(H):
    for j in range(W):
        if is_digit(s[i][j]):
            bomb = [int(s[i][j]), i, j]
            bombs.append(bomb)


for bomb in bombs:
    effect_size, b_i, b_j = bomb
    # up
    new_i = max(b_i-effect_size, 0)
    for i in range(new_i, b_i+1):
        if s[i][b_j] == "#":
            break
        else:
            s[i][b_j] = "B"

    # bottom
    new_i = min(b_i+effect_size, H)
    for i in range(b_i, new_i+1):
        if s[i][b_j] == "#":
            break
        else:
            s[i][b_j] = "B"

    # right
    new_j = min(b_j+effect_size, W)
    for j in range(b_j, new_j+1):
        if s[b_i][j] == "#":
            break
        else:
            s[b_i][j] = "B"
    # left
    new_j = max(b_j-effect_size, 0)
    for j in range(new_j, b_j+1):
        if s[b_i][j] == "#":
            break
        else:
            s[b_i][j] = "B"

# count enemies
enemies = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == 'X':
            enemies += 1

# result
if enemies == 0:
    print("YES")
else:
    print("NO")


