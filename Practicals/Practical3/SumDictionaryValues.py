# Write a Program to find sum of all values in a dictionary

dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
sum = 0

for val in dict.values():
    sum = sum + val

print("Sum: ", sum)
