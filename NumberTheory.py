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

# 3. Prime Number (New Approach)
from math import sqrt

def func(n):
    if n == 0  or n == 1:
        return False
    
    if n == 2 or n == 3:
        return True
    
    if n%2 == 0 or n%3 == 0:
        return False
        
    print("int(sqrt(n))+1", int(sqrt(n))+1)
    for i in range(5, int(sqrt(n))+1):
        print(n, i)
        if n%i == 0 or n%(i+2) == 0:
            return False
            
    return True

n = 431
print(f"Is {n} prime? - {func(n)}")

# 4. Sieve of Eratosthenes
from math import sqrt

def genprimes(n):
    primes = [True]*(n+1)
    primes[0]=False
    primes[1]=False
    for i in range(2, int(sqrt(n))+1):
        if primes[i] == True:
            for i in range(i*i, n+1, i):
                primes[i] = False
    
    for i in range(0, len(primes)):
        if primes[i] == True:
            print(i, end="\t")

genprimes(50)
