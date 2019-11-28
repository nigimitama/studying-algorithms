# N = int(input())
# S = [input() for x in range(N)]

N=8
S=['7777', '2229', '5566', '2669', '1689', '1333', '1189', '3588']

i = 2
results = []
for i in range(N):
    res = {}
    for j in range(4):
        res[S[i][j]] = []

    for key in res.keys():
        for j in range(4):
            is_same = S[i][j] == key
            if is_same:
                res[key].append(S[i][j])
    result_list = []
    result = None
    for key in res.keys():
        l = len(res[key])
        if l == 2:
            result_list.append('One Pair')
        if l == 3:
            result = 'Three Card'
        if l == 4:
            result = 'Four Card'

    n_pair = sum([1 for e in result_list if e == 'One Pair'])
    if n_pair == 1:
        result = 'One Pair'
    if n_pair == 2:
        result = 'Two Pair'
    if (n_pair != 2) & (result is None):
        result = 'No Pair'
    
    results.append(result)

results
