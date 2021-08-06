n = 558823 # Student ID
# Ans = 31 = 3+1 = 4
# Output: D

temp = n
s = 0

while True:
    if temp >= 0 and temp <= 26:
        print(s)
        break

    s = 0
    while temp > 0:
        s += temp%10
        temp = int(temp / 10)
    temp = s
