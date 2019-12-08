S = input()

words = ["dream", "dreamer", "erase", "eraser"]
has_word = []
for word in words:
    flag = 1 if word in S else 0
    has_word.append(flag)

