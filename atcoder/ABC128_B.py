# N = list(map(int,input().split()))
N = int(input())
input_line = [input() for i in range(N)]

ix = []
S = []
P = []
D = []
for i in range(N):
    ix.append(i)
    S_i, P_i = list(input_line[i].split())
    P_i = int(P_i)
    S.append(S_i)
    P.append(P_i)
    D.append([i, S_i, P_i])
    
print(f"S:{S}")
print(f"P:{P}")
print(f"D:{D}")


D = [[0, 'khabarovsk', 20], [1, 'moscow', 10], [2, 'kazan', 50], [3, 'kazan', 35], [4, 'moscow', 60], [5, 'khabarovsk', 40]]

D[0][0]

