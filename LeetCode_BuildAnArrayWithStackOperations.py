n = 3
target=[1, 3]
result = []
arr = []
for i in range(n):
    if arr != target:
        arr.append(i+1)
        result.append("Push")
    else:
        break
    if i+1 not in target:
        arr.remove(i+1)
        result.append("Pop")
        
print(result)
