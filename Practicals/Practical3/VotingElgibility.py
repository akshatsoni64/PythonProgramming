# Write a Program to Check is user is eligible for voting


def eligiblilty(age):
    return True if age > 18 and age < 100 else False


age = int(input("Enter Age: "))

print("Elgible") if eligiblilty(age) else print("Not Eligible")
