def singleNumber(self, nums):
    d = {}
    for num in nums:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1
    d = sorted(d.items(), key=lambda k:k[1])
    return d[0][0]


print(
    singleNumber([2,2,1])
)
