class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=nums.copy()
        for i in nums:
            anth=target-i
            left.pop(0)
            if anth in left:
                return nums.index(i), nums.index(anth)
            else:
                continue
            
            
