class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = ''.join([str(nums[i]) for i in range(len(nums))]).split('0')
        max1 = 0
        for i in range(len(t)):
            if len(t[i]) > max1:
                max1 = len(t[i])
        return max1

##another code
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        max1 = 0
        for num in nums:
            if num == 1:
                cnt += 1
                max1 = max(max1, cnt)
            else:
                cnt = 0
        return max1
