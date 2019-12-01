inputs = [input() for i in range(2)]
N = int(inputs[0])
A = inputs[1].split()
A = [int(i) for i in A]

yakusuu = []
for i in range(1,max(A)+1): 
    amari = [a % i for a in A]
    if sum(amari) == 0:
        yakusuu.append(i)

print(max(yakusuu))