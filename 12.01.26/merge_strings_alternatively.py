class Solution(object):
    def mergeAlternately(self, word1, word2):
        w1 = list(word1)

        idx = 0
        for i in range(len(word2)):
            w1.insert(idx+i+1, word2[i])
            idx += 1
        
        return ''.join(w1)
