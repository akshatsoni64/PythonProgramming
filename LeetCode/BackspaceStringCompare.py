S = "a##c"
T = "#a#c"
s = []
t = []

for c in S:
    if c == "#":
        if len(s) > 0:
            s.pop()
    else:
        s.append(c)

for c in T:
    if c == "#":
        if len(t) > 0:
            t.pop()
    else:
        t.append(c)

print(s == t)
