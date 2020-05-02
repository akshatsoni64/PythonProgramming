d = {1: 'Jimmy', 2: 'Alex', 3: 'John', 4: 'Mike'}


print("1st name is "+d[1])
print("2nd name is "+d.get(4))
print(d)
d[3] = "Edward"
print("New Dictionary: ")
print(d)
print(d.keys())
print(d.values())
print("Length of Dictionary: ")
print(len(d))
d[5] = "Monster"
print(len(d))
d.pop(5) # removes the specified item given in the index
print(len(d))
d.popitem() # removes the la`st item
print(len(d))
del d[3] # deleted the item of the specified index
print(len(d))
d.clear() # clears the list, deletes all the items
print(len(d))
