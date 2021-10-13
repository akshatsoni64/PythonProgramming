n = 10
queries = [
[2, 3, 603],
[1, 1, 286],
[4, 4, 882]
]
arr = [0 for i in range(n)]
for q in queries:
    print(arr[ q[0]-1 : q[1] ])
    arr[
        q[0]-1: q[1]
    ] = list(
        map(
            lambda x: x + q[2],
            arr[
                q[0]-1 : q[1]
            ]
        )
    )
    print(arr, len(arr))

#################################################
    
n = 10
queries = [
[2, 3, 603],
[1, 1, 286],
[4, 4, 882]
]
arr = [0 for i in range(n)]
for q in queries:
    for i in range(q[0]-1, q[1]):
        print(arr[i], end=",")
        arr[i] += q[2]
    print()
    print(arr, len(arr))
