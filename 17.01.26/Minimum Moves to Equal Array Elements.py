class Solution:
    def minMoves(self, a):
        m=min(a)
        return sum(x-m for x in a)
