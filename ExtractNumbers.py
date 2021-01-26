# Note: We only have to extract complete numbers, Float numbers will be considered as 2 different complete numbers

string = "I will eat 2 burgers 2345 fries & 1.25 cokes l8r9 aa"
numbers = []
for val in string.split(" "):
    if str.isdigit(val):
        numbers.append(val)
    else:
        # Check for Float Numbers
        if '.' in val: 
            for digit in val.split('.'):
                if str.isdigit(digit):
                    numbers.append(digit)
        # Non Float Values
        else: 
            add = 0
            # Check every character inside string
            for i in range(len(val)): 
                # Consecutive Numbers
                if ord(val[i]) in range(48, 58): 
                    if add > 0:
                        add = (add*10) + int(val[i])
                    # Numbers mixed with character [a2bc3]
                    else: 
                        add += int(val[i])
                    if i == len(val)-1: 
                        numbers.append(add)
                else:
                    if add > 0:
                        numbers.append(add)
                    add = 0

print(len(numbers))
print(numbers)
