q = []

def traverse(node):
    print(node, end=" ")
    if node in adl.keys():
        for val in adl[node]:
            if visited[val] != True:
                q.append(val)
                visited[val] = True
    if len(q) > 0:
        traverse(q.pop(0))
    else:
        return

adl = {
    0: [1, 2, 3],
    2: [4],
    3: [5, 7],
    5: [6]
}

visited = {
    0: False,
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    7: False,
}


traverse(0)
