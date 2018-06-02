class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rownums = len(nums)
        colnums = len(nums[0])
        if r*c != rownums*colnums:
            return nums
        if c == 0:
            return []*r

        nums_new = []
        for i in range(rownums):
            nums_new = nums_new + nums[i]
        re_nums = []
        for i in range(r):
             re_nums.append(nums_new[c*i:c*(i+1)])
        return re_nums

##another code
class Solution(object):
    def matrixReshape(self, nums, r, c):
        if len(nums) * len(nums[0]) != r * c:
            return nums
        if c == 0:
            return [] * r

        res = []
        sub = []
        for row in nums:
            for num in row:
                sub.append(num)
                if len(sub) == c:
                    res.append(sub)
                    sub = []
        return res
