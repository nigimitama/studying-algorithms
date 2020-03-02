s = input()

LETTERS_A = "BCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_C = "ABDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0
is_ok = None
c1, c2 = False, False
for i in range(len(s)):
    if i == 0:
        c1 = (s[i] == "A")
        if s[i] in LETTERS_A:
            is_ok = False
    if (2 <= i) and (i <= len(s)-2):
        if s[i] == "C":
            count += 1
            c2 = (count == 1)
        if s[i] in LETTERS_C:
            is_ok = False
        
if c1 and c2 and (is_ok is not False):
    is_ok = True
    print("AC")
else:
    print("WA")
