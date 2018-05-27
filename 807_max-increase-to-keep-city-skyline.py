# -*-coding:utf-8 -*-

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        addsum = 0
        gridT = [[y[x] for y in grid] for x in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                minmax = min([max(grid[i]), max(gridT[j])])
                if grid[i][j] < minmax:
                    addsum = addsum + minmax - grid[i][j]
        return addsum

#another function
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max1 = []#记录grid中每行的最大值
        max2 = [0 for i in range(len(grid[1]))]#记录grid中每列的最大值
        increase_high = 0
        for i in range(len(grid)):
            max1.append(max(grid[i]))
            for j in range(len(grid[i])):
                max2[j] = max(max2[j], grid[i][j])
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                increase_high += min(max1[i],max2[j])-grid[i][j]
        return increase_high
