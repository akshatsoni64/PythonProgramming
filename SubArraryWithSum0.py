# ip = "4 2 0 1 6"
ip = "4 2 -3 1 6"
l = list(map(int, ip.split(" ")))
s = 0

l.sort()
op = []

for n in l:
    if s <= 0 and s+n <= 0:
        s += n
        op.append(n)

print(op)
