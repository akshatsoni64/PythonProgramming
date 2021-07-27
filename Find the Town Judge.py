n = 3
trust = [[1,3],[2,3]]

temp = {}

for edge in trust:
    if edge[0] in temp.keys():
        temp[edge[0]] += 1
    else:
        temp[edge[0]] = 1

    if edge[1] in temp.keys():
        temp[edge[1]] += 1
    else:
        temp[edge[1]] = 1
        
if max(temp.values())
print(temp)
