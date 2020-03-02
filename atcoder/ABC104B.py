s = input()

LETTERS_A = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_C = "ABDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
is_ok = True
c1, c2 = False, False
for i in range(len(s)):
    if i == 0:
        c1 = (s[i] == "A")
        if s[i] in LETTERS_A:
            is_ok = False
    elif (2 <= i) and (i <= len(s)-2):
        if s[i] == "C":
            count += 1
        if s[i] in LETTERS_C:
            is_ok = False
    elif s[i] in LETTERS:
        is_ok = False
        
c2 = (count == 1)
if c1 and c2 and is_ok:
    print("AC")
else:
    print("WA")
