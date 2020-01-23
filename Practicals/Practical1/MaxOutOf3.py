# 2 Write a program to get the maximum number out of three numbers
a, b, c = input("Enter Three Numbers: ").split()
a, b, c = int(a), int(b), int(c)

if a > b and a > c:
    print("A is Max")
elif b > a and b > c:
    print("B is Max")
else:
    print("C is Max")
