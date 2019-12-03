A, B = list(map(int, input().split()))

def last_digit(x):
    return x % 10

ans = ""
for n in [100, 10, 1]:
    a = last_digit(A // n) + last_digit(B // n)
    ans += str(last_digit(a))
print(ans)


