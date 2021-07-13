"""
    # Adjacency list
    [
        (0, [1, 2, 3]),
        (2, 4),
    ]
    # Visited Map
    {
        0: 0/1
        1: 0/1
        2: 0/1
        3: 0/1
        4: 0/1
    }
    # Traversal array
    [0, 1, 2, 3, 4]
"""
op = []

def traverse(node):
    if visited[node] is not True:
        visited[node] = True
        op.append(node)
        if node in adl.keys():
            for nodes in adl[node]:
                traverse(nodes)

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
print(op)

# Output: [0, 1, 2, 4, 3, 5, 6, 7]
