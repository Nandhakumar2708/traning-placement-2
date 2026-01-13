class Solution(object):
    def sortSentence(self, s):
        sentence = s.split(" ")
        res = ["" for _ in range(len(sentence))]
        for s in sentence:
            index = int(s[-1])
            res[index - 1] += s[:len(s) - 1]
        
        return " ".join(res)
