N = int(input())
scores = [input().split() for i in range(N)]

is_pass = []
for score in scores:
    tscore = sum([int(score[i]) for i in range(1,5+1)])
    if score[0] == "l":
        sscore = sum([int(score[i]) for i in [4,5]])
    else:
        sscore = sum([int(score[i]) for i in [2,3]])
    
    if (tscore >= 350) and (sscore >= 160):
        is_pass.append(True)
        
print(sum(is_pass))