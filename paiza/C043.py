N = int(input())
a = [input() for i in range(1)]
a = list(map(int, a[0].split()))

unique_a = list(set(a))
unique_a.sort()
max_count = 0
max_a = []
for a_i in unique_a:
    a_count = a.count(a_i)
    if a_count > max_count:
        max_count = a_count
        max_a = [a_i]
    elif a_count == max_count:
        max_a.append(a_i)

print(" ".join(map(str, max_a)))