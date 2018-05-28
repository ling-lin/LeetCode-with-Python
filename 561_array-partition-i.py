class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(len(nums)/2):
            result += nums[2*i]
        return result

##another brief code
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])
