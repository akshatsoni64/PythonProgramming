# 6.2 - W. A. P. to find factorial using while loop
fact = 1
number = int(input("Enter Number: "))
while number > 0:
    fact *= number
    number -= 1

print(fact)
