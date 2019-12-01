N, K = list(map(int, input().split()))
input_line = [input() for i in range(1)]
a = list(map(int, input_line[0].split()))

count = 0
for j in range(2,N+1):
    print(f"j:{j}")
    for i in range(0,N):
        print(f"i:{i}")
        print(f"sum: {sum(a[i:i+j])}")
        if sum(a[i:i+j]) >= K:
            count += 1
print(count)