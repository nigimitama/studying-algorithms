n = int(input())
dishes = [input() for _ in range(n)]

n_melon = 0
eat_count = 0
is_ready = True
for dish in dishes:
    if eat_count > 0:
        is_ready = False
    else:
        is_ready = True

    if (dish == "melon") and is_ready:
        n_melon += 1
        eat_count = 10
    else:
        eat_count -= 1
    
print(n_melon)