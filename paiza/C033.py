inputs = ['ball', 'strike', 'ball', 'strike', 'strike']

b_count = 0
s_count = 0

for i in range(len(inputs)):
    
    if inputs[i] == "ball":
        b_count += 1
    else:
        s_count += 1

    if b_count >= 4:
        print("fourball!")    
    elif s_count >= 3:
        print("out!")
    else:
        print(inputs[i]+"!")
