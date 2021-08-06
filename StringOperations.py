"""str = "Let it be, let it be, let it be"
# str = input("Enter String: ")
# print(str.capitalize())
# print(str.count('i'))
result = str.find('let it')
print("Substring 'let it': ", result)
result = str.find('small')
print("Substring 'small': ", result)
if str.find('be,') != -1:
    print("Substring 'let it': ", result)
else:
    print("Doesn't contain substring")"""
str = "Do small things with great love"
print(str.find('small thing', 10))  # 'hings with great love'
print(str.find('small thing', 2))  # ' small things with great love'
print(str.find('o small', 10, -1))  # 'hings with great lov'
print(str.find('things', 6, 20))  # 'll things with'
