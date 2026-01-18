class Solution:
    def poorPigs(self, b, m, t):
        p=0
        while (t//m+1)**p<b:
            p+=1
        return p
