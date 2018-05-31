class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) > 1 and len(matrix[0]) > 1:
            cnt = 0
            for i in range(len(matrix)-1):
                for j in range(len(matrix[i])-1):
                    if matrix[i][j] <> matrix[i+1][j+1]:
                        cnt += 1
            return cnt == 0
        else:
            return True
