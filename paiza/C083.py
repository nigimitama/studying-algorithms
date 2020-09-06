N, R = map(int, input().split())
a = [int(input()) for _ in range(N)]

y = [int(a_i / R) for a_i in a]
max_y = max(y)
for i in range(N):
    n_dot = max_y - y[i]
    s = y[i] * "*" + n_dot * "."
    print(f"{i+1}:{s}")
