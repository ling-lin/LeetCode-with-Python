# -*- coding:utf-8 -*-

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        for i in S:
            if i in J:
                n = n+1
        return(n)

obj = Solution()
obj.numJewelsInStones('aA', 'aAAbbbb')
