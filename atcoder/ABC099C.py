N = int(input())
# wakaran
def gcd(a, b):
    r = a % b
    return gcd(b, r)
