N = int(input())
rows = [list(map(int, input().split())) for _ in range(N)]
rows = [[0, 0, 0]] + rows

def is_even(x):
    return x % 2 == 0

is_can = True
for i in range(1, N+1):
    diff_t = rows[i][0] - rows[i-1][0]
    diff_x = abs(rows[i][1] - rows[i-1][1])
    diff_y = abs(rows[i][2] - rows[i-1][2])
    if diff_t == 1:
        if (diff_x == 0) and (diff_y == 0):
            is_can = False
            break
    if (diff_x > diff_t):
        is_can = False
        break
    elif (diff_y > diff_t):
        is_can = False
        break

    if is_even(diff_t):
        if not is_even(diff_x + diff_y):
            is_can = False
            break  
    else:
        if is_even(diff_x + diff_y):
            is_can = False
            break

if is_can:
    print("Yes")
else:
    print("No")