s = input()

boin = ["a", "e", "i", "o", "u",  "A", "E", "I", "O", "U" ]
new_s = ""
for i in range(len(s)):
    if s[i] not in boin:
        new_s += s[i]
print(new_s)
