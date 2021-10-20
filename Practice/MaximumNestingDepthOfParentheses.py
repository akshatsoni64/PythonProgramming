def maxDepth(self, s: str) -> int:
    cm = m = 0
    for b in s:
        if b == '(':
            cm += 1
            m = max(m, cm)
        elif b == ')':
            if cm > 0:
                cm -= 1

    return -1 if cm != 0 else m


print(
  maxDepth(
    "(1)+((2))+(((3)))"
  )
)
