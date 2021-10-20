def rotateLeft(d, arr):
    return arr[d:]+arr[:d]


print(rotateLeft(3, [1, 2, 3, 4, 5]))
