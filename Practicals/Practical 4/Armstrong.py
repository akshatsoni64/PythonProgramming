# 2 - W. A. P. to check if a number is armstrong or not

n = int(input("Enter a number:"))
sum = 0
temp = n
while temp > 0:
    a = temp % 10
    sum += a ** 3
    temp //= 10

print(n, "Armstrong Number") if n == sum else print(n, "Not Armstrong Number")
