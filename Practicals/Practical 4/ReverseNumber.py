# 4 - W. A. P. to Reverse a Number

n = int(input("Enter a number: "))
rev = 0
while (n > 0):
    rem = n % 10
    rev = (rev * 10) + rem
    n = n // 10
print("Reversed Number: ", rev)
