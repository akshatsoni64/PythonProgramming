a = input("Enter Three Number(Separated by single space): ").split(' ')
# print(a)

for i in range(len(a)):
    for j in range(i,(len(a))):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

# print(a)
print("Min: ", a[0])
print("Max: ", a[-1])
