class Solution:
    def frequencySort(self, s):
        from collections import Counter
        c=Counter(s)
        return ''.join(k*v for k,v in c.most_common())
