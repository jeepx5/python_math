class Solution:
    def twoSum(self, nums, target):
        left=nums.copy()
        for i in nums:
            anth=target-i
            left.pop(0)
            if anth in left:
                print(left.index(anth))
                return nums.index(i), (nums.index(i)+1+left.index(anth))
            else:
                continue
