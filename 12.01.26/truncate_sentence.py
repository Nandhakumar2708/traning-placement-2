class Solution(object):
    def truncateSentence(self, s, k):
        l=[]
        for i in s.split():
            l.append(i)
        return " ".join(l[:k])
