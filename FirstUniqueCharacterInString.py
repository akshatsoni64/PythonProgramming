def firstUniqChar(self, s: str) -> int:
    d = {}
    for c in s:
        if c not in d.keys():
            d[c] = s.count(c)
    x = {}
    for k, v in d.items():
        if v == 1:
            x[k] = v
    if x:
        ch = sorted(x.items(), key=lambda x: x[1])[0][0]
        return s.index(ch)
    else:
        return -1


print(firstUniqChar("leetcode"))
