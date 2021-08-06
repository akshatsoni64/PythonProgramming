"""
There are number of friends, they want to attend a party
But they can either go to party all alone or in a pair
Give the number of ways they can go to the party
"""

def friends(n):
    return n if n == 1 or n == 2 else friends(n-1) + (n-1)*friends(n-2)
    
print("Number of ways they can go to party: ", friends(int(input("Enter Person Count: "))))
