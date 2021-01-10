N, M = list(map(int, input().split()))

# print(10**N // M % M)
print(pow(10, N, M*M) // M % M)

"""
解説
---

Yuuki Uchida  11:55
A mod B  は、A をBで割った余りをあわらす（通例）。
A mod B = C mod B
は、AをBで割った余りとCをBで割った余りが等しい、の意。
これを
A ≡ C (mod B)
と表す。
一般に、A ≡ C なら A-kB ≡ Cも成り立つ。（kは正の整数）
e.g.
22 ≡ 8 (mod 7) なら、k=1として
22-1*7 = 15 ≡ 8 (mod 7).

（modの説明は本質的じゃなかった…）
今回の問題を整理すると、
10**N ÷ M = p … q
p ÷ M = a … b
のbを求めてる。
12:14
（pow関数が勉強になりました）
"""