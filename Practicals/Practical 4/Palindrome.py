# 1 - W. A. P. to check palindrome using conditional statement

s1 = input("Enter String: ")
s2 = s1[::-1]
print("Palindrome") if s1 == s2 else print("Not Palindrome")
