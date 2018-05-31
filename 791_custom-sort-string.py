class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        result = ''
        for i in S:
            if i in T:
                leni = T.count(i)
                result = result+i*leni
                T = T.replace(i, '')
        return result+T
