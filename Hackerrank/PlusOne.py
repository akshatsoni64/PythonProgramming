def plusOne(self, digits):
    digit = int("".join(map(str, digits))) + 1
    return list(map(int, str(digit)))
