class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        def isPrime(n): 
            if n <= 1: 
                return False
            i = 2
            while i*i <= n: 
                if n % i == 0: 
                    return False
                i += 1
            return True
    
        cnt = 0
        for num in range(L,R+1):
            tmp = bin(num).count('1')
            if isPrime(tmp) == True:
                cnt += 1
        return cnt
