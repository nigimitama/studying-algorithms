# https://paiza.jp/works/mondai/skillcheck_archive/word_chain?language_uid=python3
n, k, m = map(int, input().split())
d = [input() for _ in range(k)]
s = [input() for _ in range(m)]


class WordChain:

    def __init__(self, d):
        self.d = d
        self.d_set = set(d)
        self.words = []

    def play(self, ):
        is_drop = False

        if i != 0:
            if not is_chained(s[i-1], s[i]):
                is_drop = True

        if w.is_duplicated(s[i]) or is_z_end(s[i]) or not w.is_in_dict(s[i]):
            is_drop = True
        return is_drop

    def is_in_dict(self, x):
        return x in self.d_set

    def is_duplicated(self, x):
        return x in self.words

    def used_word(self, x):
        if x in self.d_set:
            self.words.append(x)

    def is_chained(self, prev, x):
        return prev[-1] == x[0]

    def is_z_end(self, x):
        return x[-1] == "z"


players = list(range(1, n+1))
for i in range(n):
    if i in players:
        
w = WordChain(d)


w = WordChain(d)
for i in range(m):
    is_drop = False

    if i != 0:
        if not is_chained(s[i-1], s[i]):
            is_drop = True

    if w.is_duplicated(s[i]) or is_z_end(s[i]) or not w.is_in_dict(s[i]):
        is_drop = True

    if is_drop:
        n -= 1

    w.used_word(s[i])

print(n)
