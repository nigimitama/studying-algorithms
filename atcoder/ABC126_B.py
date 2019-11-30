S = input()
yymm_flag = False
mmyy_flag = False
if 1 <= int(S[0:2]) <= 12:
    mmyy_flag = True
if 1 <= int(S[2:4]) <= 12:
    yymm_flag = True
if (mmyy_flag == True) and (yymm_flag == True):
    print('AMBIGUOUS')
elif (mmyy_flag == True) and (yymm_flag == False):
    print('MMYY')
elif (mmyy_flag == False) and (yymm_flag == True):
    print('YYMM')
elif (mmyy_flag == False) and (yymm_flag == False):
    print('NA')
