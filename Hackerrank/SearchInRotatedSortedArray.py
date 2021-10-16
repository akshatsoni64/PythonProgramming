def search(self, nums, target):
    return nums.index(target) if target in nums else -1

print(
  search([4,5,6,7,0,1,2], 0)
)
