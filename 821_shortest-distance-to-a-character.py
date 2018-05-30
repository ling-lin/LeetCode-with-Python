class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        eindex = []
        for i in range(len(S)):
            if S[i] == C:
                eindex.append(i)
        result = []
        for i in range(len(S)):
            min_ = []
            for j in range(len(eindex)):
                min_.append(abs(eindex[j]-i))
            min_1 = min(min_)
            result.append(min_1)
        return result
