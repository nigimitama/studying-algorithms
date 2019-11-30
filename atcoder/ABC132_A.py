from collections import Counter
S = list(input())
kind = list(set(S))
result = "Yes"
for i in range(len(kind)):
    if S.count(kind[i]) != 2:
        result = "No"
print(result)