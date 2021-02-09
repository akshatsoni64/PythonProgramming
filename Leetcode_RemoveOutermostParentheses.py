string = "()()"
"(()())(())(()(()))"
# "(()())(())"
lc = rc = 0
l = []
for char in string:
    if char == "(":
        if lc > 0:
            l.append(char)
        lc += 1
    elif char == ")":
        rc += 1
        if lc == rc:
            lc = 0
            rc = 0
        else:
            l.append(char)
    print("LC:", lc, "--RC:", rc)
print(l)
"""
( ()() ) ( () )

Output
()()
()
"""

"""
( ()() ) ( () ) ( () (()) )

Output
()()
()
()
(())
"""
