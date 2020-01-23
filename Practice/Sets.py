set1 = {"Apple", "Banana", "Cherry"}
set2 = {"Potato", "Tomato"}

print("Banana" in set1)
set1.add("Mango")
print(len(set1))
set1.remove("Cherry")
print(set1)
set1.pop()
print(set1)
set3 = set1.union(set2)
print(set2)
set1.update(set2)
print(set1)
