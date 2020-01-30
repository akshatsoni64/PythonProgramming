# Write a Program to exchange two numbers without using 3rd number


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    return [a, b]


a = int(input("Enter A: "))
b = int(input("Enter B: "))

print("Original: A-", a, ", B-", b)
a, b = swap(a, b)
print("Swapped: A-", a, ", B-", b)
