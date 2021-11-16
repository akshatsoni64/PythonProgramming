import re

s = "A man, a plan, a canal: Panama"

temp = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        
print(temp == temp[::-1])
