N = int(input())
L = [input() for i in range(1)]
a = list(map(int, L[0].split()))

alice = []
bob = []
for i in range(N):
    a.sort(reverse=True)
    if i % 2 == 0:
        alice.append(a[i])
    else:
        bob.append(a[i])
print(sum(alice) - sum(bob))