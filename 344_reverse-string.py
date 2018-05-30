class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = list(s)
        lens1 = len(s1)
        hlens1 = lens1//2
        for i in range(hlens1):
            tmp = s1[i]
            s1[i]=s1[lens1-1-i]
            s1[lens1-1-i]=tmp
        return ''.join(s1)

##another brief code
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
