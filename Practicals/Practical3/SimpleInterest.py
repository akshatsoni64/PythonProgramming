# Write a Program using Function to calculate simple interest, accepts 3 args. and returns the simple interest


def interest(p, r, t):
    return (p * r * t) / 100


p = int(input("Enter Amount: "))
r = int(input("Enter Interest Rate: "))
t = int(input("Enter Time Period: "))

print("Interest Amount: ", interest(p, r, t))
