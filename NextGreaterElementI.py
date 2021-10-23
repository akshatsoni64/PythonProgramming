def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    hash_map = dict()
    stack = nums2[0:1]

    for num in nums2[1:]:
        while stack and stack[-1] < num:
            hash_map[stack.pop()] = num
        stack.append(num)
    return [hash_map.get(num, -1) for num in nums1]
