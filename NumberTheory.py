# 1. GCD, LCM
def gcd(a, b):
    print(f"GCD - a: {a} b: {b}")
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    print(f"LCM - a: {a} b: {b}")
    prod = a*b
    hcf = gcd(a, b)
    return prod//hcf

print("GCD:", gcd(5, 10))
print("\nLCM:", lcm(5, 10))

# 2. Divisors
from math import sqrt
def fun1(n):
    return list(set(x for x in range(1, n+1) if n%x == 0))

def fun2(n):
    res = []
    for i in range(1, int(sqrt(n))):
        res.extend([i, int(n/i)])
    return res
ans = fun2(18)
print(*ans)
