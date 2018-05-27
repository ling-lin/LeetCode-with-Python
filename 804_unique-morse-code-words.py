# -*- coding:utf-8 -*-

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = [chr(i) for i in range(97,123)]
        morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        t = {k:v for (k,v) in zip(alphabet, morsecode)}
        result = []
        for kk in range(len(words)):
            wordsmorse = ''
            for j in words[kk]:
                wordsmorse = wordsmorse + t[j]
            result.append(wordsmorse)
        cnt = len(set(result))
        return cnt  
