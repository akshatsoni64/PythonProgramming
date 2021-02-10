s = "(()())(())(()(()))"
s = "()()"
result = []
l = []
lc = rc = 0
for c in s:
    l.append(c)
    if c == "(":
        lc += 1
    elif c == ")":
        rc += 1
    if lc > 0 and rc > 0 and lc == rc:
        l.pop(-1)
        l.pop(0)
        result.extend(l)
        l = []
        lc = rc = 0
    
    
string = ""
for c in result:
    string += c
    
print(string)
