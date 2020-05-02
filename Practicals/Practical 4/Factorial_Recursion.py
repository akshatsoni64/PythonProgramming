# 6.1 - W. A. P. to find factorial using recursion
def fact(number):
    return number if number ==1 else number * fact(number - 1)


num = int(input("Enter Number: "))
print("Factorial: ", fact(num))
