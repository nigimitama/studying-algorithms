"""
B012:チェックディジットの問題にチャレンジ！ | プログラミング学習サービス【paizaラーニング】
https://paiza.jp/challenges/41/show
"""

def calc(Di):
    Di = list(Di)
    even_list = []
    odd_list = []
    for i in range(1,len(Di),2):
        odd_list.append(int(Di[i]))
    for i in range(0,len(Di),2):
        even_list.append(int(Di[i]) * 2)
    even_list_2 = []
    for ei in even_list:
        if ei >= 10:
            eil = list(str(ei))
            even_list_2.append(int(eil[0]) + int(eil[1]))
        else:
            even_list_2.append(ei)
    # sum
    even = sum(even_list_2)
    odd = sum(odd_list)
    y = even + odd
    # print(y)
    if y % 10 == 0:
        ans = True
    else:
        ans = False
    return ans


def get_ans(D):
    for i in range(10):        
        ans = calc(D.replace("X",str(i)))
        if ans:  
            
            break
    return(i)


N = input()
D = [input() for i in range(int(N))]
for Di in D:
    print(get_ans(Di))





D  = ["846087729128569X"]
for Di in D:
    print(get_ans(Di))



Di  = "0911804224781891"
Di = list(Di)
Di = Di[0:len(Di)]
Dl = Di.copy()
for j in range(len(Di)): # characters
    Dl[j] = int(Di[j]) % 2 == 0 # bool    
even_list = []
odd_list = []
for p in range(len(Dl)):
    if Dl[p]:
        even_list.append(int(Di[p]))
    else:
        odd_list.append(int(Di[p]))
# 2 times
even_list = [s * 2 for s in even_list]
even_list_2 = []
for ei in even_list:
    if ei >= 10:
        eil = list(str(ei))
        even_list_2.append(int(eil[0]) + int(eil[1]))
    else:
        even_list_2.append(ei)
# sum
even = sum(even_list_2)
odd = sum(odd_list)
y = even + odd
print(y)
if y % 10 == 0:
    ans = True
else:
    ans = False
ans





