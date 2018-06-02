class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums[0]
        for i in range(1,len(nums)):
            A = A^nums[i]
        return A
