class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result=[]
        S_ = S.split(' ')
        vowel = ['a','e','i','o','u']
        for i in range(len(S_)):
            word = list(S_[i])
            if word[0].lower() not in vowel:
                result.append(''.join(word[1:])+''.join(word[0])+'ma'+'a'*(i+1))
            else:
                result.append(''.join(word)+'ma'+'a'*(i+1))
        return ' '.join(result)
