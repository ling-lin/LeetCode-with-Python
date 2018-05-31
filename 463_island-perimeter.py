class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = [[0]*len(grid[0])]+grid+[[0]*len(grid[0])]
        strips = 0
        for i in range(len(grid)):
            grid[i] = [0] + grid[i] + [0]
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                if grid[i][j] == 1:
                    strips = strips + 4 - (grid[i-1][j]+grid[i+1][j]+grid[i][j-1]+grid[i][j+1])
        return strips
