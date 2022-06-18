def goodString (N, Q, S, arr, ranges):
    S = list(S)
    for idx in range(len(arr)):
        pos = arr[idx]
        S[pos-1] = '_'
        # print("\n", pos, S)
        c = 0
        for [a, b] in ranges:
            d = {}
            flag = True
            for i in range(a-1, b):
                char = S[i]
                if char != '_':
                    # print("CHAR & I", char, i, end="\t")
                    i = i-1
                    try:
                        d[char] += 1
                        flag = False
                        # print("BINGO", d)
                        break
                    except:
                        d[char] = 1
            # print("Flag:", flag, d, '"', a, '-', b, '"')
            if flag:
                c += 1
        # print("Count:", c)
        if c == Q:
            break
    # print(S)
    return idx+1
  
print(
    goodString(
        8, 3, 'abbabaab',
        [6, 3, 5, 1, 4, 2, 7, 8],
        [[1, 3], [4, 7], [3, 5]]
    )
)
