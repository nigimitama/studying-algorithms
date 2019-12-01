N = int(input())
b = [input() for x in range(N)]

result = []
for col in range(4):    
    if sum([int(b_i[col]) for b_i in b]) % 2 == 0:
        result.append("0")
    else:
        result.append("1")
print("".join(result))