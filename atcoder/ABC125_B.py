# Vi-Ci> 0である限り足していく
inputs = [input() for i in range(3)]
N = int(inputs[0])
V = inputs[1].split()
C = inputs[2].split()

TR = 0
for i in range(0,N):
    R = int(V[i]) - int(C[i])
    if R > 0:
        TR = TR + R

print(TR)