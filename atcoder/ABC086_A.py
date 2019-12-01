A, B = list(map(int, input().split()))
product = A*B
if product % 2 == 0:
    print("Even")
else:
    print("Odd")