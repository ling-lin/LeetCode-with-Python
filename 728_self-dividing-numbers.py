class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            stri = str(i)
            lenstri = len(stri)
            selfnum =[]
            selfdiv = []
            for j in range(lenstri):
                selfnum.append(int(stri[j]))
            if selfnum.count(0) == 0:
                for j in range(len(selfnum)):
                    selfdiv.append(i%selfnum[j])
            if selfdiv.count(0) == len(selfnum):
                result.append(i)
        return result

##another elegant function
class Solution(object):
    def selfDividingNumbers(self, left, right):
        is_self_dividing = lambda num: '0' not in str(num) and all(num % int(digit) == 0 for digit in str(num))
        return filter(is_self_dividing, range(left, right + 1))
