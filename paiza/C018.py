n = int(input())
ab = [input().split() for _ in range(n)]
m = int(input())
cd = [input().split() for _ in range(m)]

recipe = {a: int(b) for a, b in ab}
ingredients = {c: int(d) for c, d in cd}

min_n_times = 10**9
for name in recipe.keys():
    if name in ingredients:
        n_times = ingredients[name] // recipe[name]
        if n_times < min_n_times:
            min_n_times = n_times
    else:
        min_n_times = 0
        break
print(min_n_times)
