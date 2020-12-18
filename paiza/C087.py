n = input()

def reverse(n: str) -> str:
    return n[::-1]

def is_repeat(n: str) -> str:
    return n == reverse(n)

while not is_repeat(n):
    n = int(n) + int(reverse(n))
    n = str(n)

print(n)
