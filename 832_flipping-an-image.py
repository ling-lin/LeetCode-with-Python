# -*- coding:utf-8 -*-

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            n = len(A[i])
            for j in range(n//2):
                tmp = A[i][j]
                A[i][j] = A[i][n-1-j]
                A[i][n-1-j] = tmp
        for i in range(len(A)):
            n = len(A[i])
            for j in range(n):
                A[i][j] = 1-A[i][j]
        return A
        
obj = Solution()
B = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
obj.flipAndInvertImage(B)
