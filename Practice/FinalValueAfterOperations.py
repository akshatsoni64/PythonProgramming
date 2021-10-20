def finalValueAfterOperations(self, operations):
    x = 0
    for op in operations:
        if op in ['++X', 'X++']:
            x += 1
        else:
            x -= 1
    return x


print(
    finalValueAfterOperations(['++X', 'X++', '--X', 'X--'])
)
