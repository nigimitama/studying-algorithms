# N = list(map(int, input().split()))
N = int(input())
input_line = [input() for i in range(N)]
d = [list(map(int,i.split())) for i in input_line]
# print(f"N:{N},d:{d}")

diff = []
for i in range(1,N):
    diff_x = abs(d[i][0] - d[i-1][0])
    diff_y = abs(d[i][1] - d[i-1][1])
    diff += [[diff_x, diff_y]]

diff_x = abs(d[N-1][0] - d[0][0])
diff_y = abs(d[N-1][1] - d[0][1])
diff += [[diff_x, diff_y]]
print(f"diff: {diff}")

def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]
diff_u = get_unique_list(diff)
# print(f"unique:{diff_u}")

ans = len(diff_u)
print(ans)