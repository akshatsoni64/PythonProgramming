# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # arr = [
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 0, 2, 4, 4, 0],
    #     [0, 0, 0, 2, 0, 0],
    #     [0, 0, 1, 2, 4, 0]
    # ]
    arr = []
    sumlist = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(0, (len(arr[0])-2)):
        for j in range(0, (len(arr[1])-2)):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            sum += arr[i+1][j+1]
            sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sumlist.append(sum)

    sumlist.sort(reverse=True)

    print(sumlist[0])
