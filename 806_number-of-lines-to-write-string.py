class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        key = "abcdefghijklmnopqrstuvwxyz"
        keydict = {i:j for (i,j) in zip(key, widths)}
        line = 1
        unit = 0
        for i in S:
            if unit + keydict[i] > 100:
                line += 1
                unit = 0
            unit = unit + keydict[i]
        return [line, unit]
