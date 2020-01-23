num_sum = 0
count = 0

while count<10:
    num_sum = num_sum + count
    count = count + 1
    if count == 5:
        break

print("Sum of first ", count, "integers is: ", num_sum)