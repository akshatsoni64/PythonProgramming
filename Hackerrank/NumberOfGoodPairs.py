def numIdenticalPairs(self, nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] == nums[j] and i < j:
                count +=1
    return count


print(
    numIdenticalPairs([1,2,3,1,1,3])
)
