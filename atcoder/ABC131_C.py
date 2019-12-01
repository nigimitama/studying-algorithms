# A,B,C,D = list(map(int,input().split()))

# count = 0
# for n in range(A,B+1):
#     if n % C != 0 and n % D != 0:
#         count += 1

# print(count)





# A,B,C,D = list(map(int,input().split()))

# candiv = []
# n = 0
# while True:
#     n += 1
#     cn = C * n
#     dn = D * n
#     if (A <= cn and cn <= B):
#         candiv.append(cn)
#         print(f"cn: {cn}")
#     if (A <= dn and dn <= B):
#         candiv.append(dn)
#         print(f"dn: {dn}")
#     if cn > B and dn > B:
#         break
# print(set(candiv))
# count = len(list(set(candiv)))
# print(f"count:{count}")
# print(B - A + 1 - count)


# A,B,C,D = list(map(int,input().split()))
# if C == 1 or D == 1:
#     count = 0
# else:
#     n_diff_c_multiple = (B // C) - (A // C)
#     n_diff_d_multiple = (B // D) - (A // D)
#     def gcd(a, b):
#         if (b == 0):
#             return abs(a)
#         return gcd(b, a % b)
#     least_common_multiple = C * D / gcd(C, D)
#     n_diff_common_multiple = int((B // least_common_multiple) - (A // least_common_multiple))
#     count = n_diff_c_multiple + n_diff_d_multiple - n_diff_common_multiple
# # print(f"count:{count}")
# print(B - A + 1 - count)


A,B,C,D = list(map(int,input().split()))
def gcd(a, b):
    if (b == 0):
        return abs(a)
    return gcd(b, a % b)
least_common_multiple = C * D / gcd(C, D)
under_B = B - (B // C) - (B // D) + (B // least_common_multiple)
under_A = A - (A // C) - (A // D) + (A // least_common_multiple)
count = under_B - under_A
# print(f"under_B: {under_B}, under_A: {under_A}")
print(count)


