# https://paiza.jp/works/mondai/skillcheck_archive/lottery?language_uid=python3
b = int(input())
n = int(input())
a = [int(input()) for _ in range(n)]


class Lottery:

    def __init__(self, b):
        self.b = b
        b_str = str(b)
        b_dig = len(b_str)
        self.b4 = b_str[(b_dig - 4):]
        self.b3 = b_str[(b_dig - 3):]

    def is_hit(self, x) -> str:
        x_str = str(x)
        x_dig = len(x_str)
        x4 = x_str[(x_dig - 4):]
        x3 = x_str[(x_dig - 3):]

        if x == self.b:
            print("first")
        elif (x == self.b+1) or (x == self.b-1):
            print("adjacent")
        elif (x4 == self.b4):
            print("second")
        elif (x3 == self.b3):
            print("third")
        else:
            print("blank")


lot = Lottery(b)
for a_i in a:
    lot.is_hit(a_i)
