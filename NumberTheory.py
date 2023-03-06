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
