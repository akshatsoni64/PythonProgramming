#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0
for i in range(0, n):    
    for j in range(i, n):
        if a[i] > a[j]:
            numSwaps += 1
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            

print("Array is sorted in",numSwaps,"swaps.")
print("First Element:", a[0])
print("Last Element:", a[n-1])