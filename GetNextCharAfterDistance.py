# Calculate the distance between the given characters and get the next character after that distance (Accenture Coding Test)

def nextChar(c1, c2):
    l1 = ord(c1)
    l2 = ord(c2)
    
    print("{}: {} \n{}: {}".format(c1, l1, c2, l2))
    
    if l1 > l2:
        start = ord('a')
        end = ord('z')
        
        d1 = l2 - start
        d2 = end - l1
        
        d = d1 + d2
    
    else:
        d = l2-l1
    
    print("Distance:", d)
    return chr(l2+d)

print("Case1: {}\n".format(nextChar('a', 'f')))
print("Case2: {}".format(nextChar('m', 'f')))
