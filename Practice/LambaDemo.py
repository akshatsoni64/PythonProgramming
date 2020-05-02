# 1

double = lambda x: x * 2

print(double(3))

# 2

mylist = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), mylist))
print("Even numbers from the list: ", new_list)

# 3

new_list = list(map(lambda x: x * 2, mylist))
print("Doubled Elements: ", new_list)
