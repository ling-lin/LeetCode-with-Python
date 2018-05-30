class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bina = bin(num).split('b')[1]
        compb = []
        for i in range(len(bina)):
            if bina[i] == '1':
                compb.append('0')
            else:
                compb.append('1')
        return int(''.join(compb), 2)
