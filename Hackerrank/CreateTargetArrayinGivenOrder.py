def createTargetArray(self, nums, index):
    op = []
    for i in range(len(index)):
        op.insert(index[i], nums[i])
    return op


print(
    createTargetArray([0,1,2,3,4], [0,1,2,3,4])
)
