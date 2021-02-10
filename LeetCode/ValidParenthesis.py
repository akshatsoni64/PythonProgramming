s = "[()]" # Valid
# s = "]{([)}" #Invalid
temp = []
counter = 0
for sym in s:
    if sym == "(" or sym == "[" or sym ==  "{":
        temp.append(sym)
        counter -= 1
    else:
        counter += 1
        if len(temp) > 0:
            ele = temp[-1]
        else:
            break

        if ele == "(" and sym == ")":
            temp.pop();
        elif ele == "[" and sym == "]":
            temp.pop();
        elif ele == "{" and sym == "}":
            temp.pop();
        else:
            break
print(True if abs(counter) + len(temp) == 0 else False)
