class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies)/2 > len(set(candies)):
            return len(set(candies))
        else:
            return len(candies)/2
