class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        lenw = len(words)
        words_ = [words[i].lower() for i in range(lenw)]
        keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
        for i in range(lenw):
            a = set(words_[i])
            for j in range(3):
                b = set(keyboard[j])
                if a&b == a:
                    result.append(words[i])
        return result

