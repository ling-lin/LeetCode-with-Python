class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = s.split(' ')
        result = []
        for i in range(len(s1)):
            result.append(s1[i][::-1])
        return ' '.join(result)

##another elegant code
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s[::-1]
        s=a.split(' ')
        s=s[::-1]
        return " ".join(s)
