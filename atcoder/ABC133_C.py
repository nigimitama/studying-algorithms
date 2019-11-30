# L,R = list(map(int,input().split()))
# Y = []
# for i in range(L, R):
#     for j in range(i+1, R+1):
#         Y.append((i * j) % 2019)
# print(min(Y))

# L,R = list(map(int,input().split()))
# Y = []
# j = 1
# for i in range(L, R):
#     if i == 0:
#         Y.append((i * j) % 2019)
#     elif i * j == 2019:
#         Y.append([0])
#     else:
#         for j in range(i+1, R+1):
#             Y.append((i * j) % 2019)
# print(min(Y))




# L,R = list(map(int,input().split()))

# def f(L,R):
#     mod_min = L*R % 2019
#     for i in range(L, R):
#         for j in range(i+1, R+1):
#             mod = (i * j) % 2019
#             if mod < mod_min:
#                 mod_min = mod
#                 if mod_min == 0:
#                     break
#     return mod_min
# print(f(L,R))



# WA answer
L,R = list(map(int,input().split()))
def wa(L,R):
    mod_min = 2019
    L %= mod_min
    R %= mod_min
    for i in range(L,R):
        for j in range(i+1, R+1):
            Y = i*j % 2019
            if Y < mod_min:
                mod_min = Y
    return mod_min

L,R = 4000, 5000
print(wa(L,R))


# AC answer
# 2019で割ったあまりは2019通りしかないので，
# 2019 * 2019通りについて考えればよい
L,R = list(map(int,input().split()))
def main(L,R):
    mod_min = 2019
    if L // mod_min == R // mod_min:
        L %= mod_min
        R %= mod_min
        for i in range(L,R):
            for j in range(i+1, R+1):
                Y = i*j % 2019
                if Y < mod_min:
                    mod_min = Y
    else:
        mod_min = 0
    return mod_min
print(main(L,R))

L,R = 4000, 5000
print(main(L,R))


# L // 2019 == R // 2019でないと通用しないことへの手がかり
def is_same(i,j,mod=2019):
    l = i // mod
    r = j // mod
    print(f"i // mod : {l}, j // mod: {r}")
    a = i*j % mod
    b = (i % mod) * (j % mod)
    print(f"a: {a}, b: {b}, is_same?: {a == b}")
is_same(0,2019)
is_same(2019*2, 2019*3)
is_same(4000, 1000000)


