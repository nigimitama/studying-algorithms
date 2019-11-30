H,W,N = list(map(int,input().split()))
input_line = [input() for i in range(3)]
# print(f"H:{H},W:{W},N:{N}")
# print(input_line)
s_r, s_c = list(map(int, input_line[0].split()))
S = input_line[1]
T = input_line[2]

def koma(s_r, s_c, x):
    if x == "L":
        s_c -= 1
    elif x == "R":
        s_c += 1
    elif x == "U":
        s_r -= 1
    elif x == "D":
        s_r += 1
    return [s_r, s_c]

result = "YES"
for i in range(0,N):
    # takahashi's turn
    print(S[i])
    if i % 3 != 0:
        s_r, s_c = koma(s_r, s_c, S[i])
    print(f"{s_r},{s_c}")
    
    # if out of field
    if (s_r > H)|(s_c > W):
        result = "NO"
        break

    # aoki's turn
    print(T[i])
    if i % 3 != 0:
        s_r, s_c = koma(s_r, s_c, T[i])
    print(f"{s_r},{s_c}")

print(result)