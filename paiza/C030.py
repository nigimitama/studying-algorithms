H, W = list(map(int, input().split()))
ndarray = [list(map(int, input().split())) for i in range(H)]

for row in ndarray:
    print_row = []
    for col in row:
        x = "1" if col >= 128 else "0"
        print_row.append(x)
    print(" ".join(print_row))