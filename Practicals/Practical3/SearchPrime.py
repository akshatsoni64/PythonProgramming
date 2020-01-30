# Write a Program to Search Prime Numbers Between 10-20

for i in range(10, 20):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
