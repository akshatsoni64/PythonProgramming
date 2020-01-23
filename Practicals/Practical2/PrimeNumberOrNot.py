number = int(input("Enter Number: "))
flag = 0
for i in range(2, number):
    if number % i == 0:
        flag = 1
        break
    else:
        flag = 0

print("Prime") if flag == 0 else print(" Not Prime")
