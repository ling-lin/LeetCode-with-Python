class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(len(findNums)):
            greater = []
            idx = nums.index(findNums[i])
            for j in range(idx+1, len(nums)):
                if findNums[i] < nums[j]:
                    greater.append(nums[j])             
            if len(greater) > 0:
                result.append(greater[0])
            else:
                result.append(-1)
        return result
