class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        for i in range(len(ops)):
            if i > 0 and ops[i] == "C":
                points.remove(points[-1])
            elif i > 0 and ops[i] == "D":
                points.append(points[-1]*2)
            elif i > 0 and ops[i] == "+":
                points.append(points[-1] + points[-2])
            else:
                points.append(int(ops[i]))
        return sum(points)
