class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        binary = bin(n).split('b')[1]
        lens = len(binary)
        n = 0
        for i in range(lens):
            if (i+1+int(binary[i])) % 2 != 0:
                n += 1
        return n == 0

##another elegant code
def hasAlternatingBits(self, n):
    return '00' not in bin(n) and '11' not in bin(n)


##another code
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        tmp = n & 1
        n >>= 1
        while n > 0:
            if (n & 1) == tmp:
                return False
            tmp = n & 1
            n >>= 1
        return True
