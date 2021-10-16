def searchInsert(self, nums, target):
    try:
        return nums.index(target)
    except:
        i = 0
        while(i < len(nums) and nums[i] < target):
            i += 1
        return i


print(
    searchInsert([1,3,5,6], 5)
)
