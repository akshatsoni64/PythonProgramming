#decimal to any base conversion
n = int(input("Enter Base: "))
num = int(input("Enter Number: "))
op = ""
while num != 0:
    rem = num % n;
    if rem > 9:
        op += str(chr(64 + (rem - 9)))
    else:
        op += str(rem)
    num = num // n

print("Output: ", op[::-1])
