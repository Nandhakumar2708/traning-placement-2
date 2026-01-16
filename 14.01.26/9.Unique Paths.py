class Solution(object):
    def uniquePaths(self, m, n):
        total_moves= m + n - 2
        r = min(m-1,n-1)
        res = 1
        for i in range(1, r+1):
            res = res * (total_moves - i + 1)/i
        return res
