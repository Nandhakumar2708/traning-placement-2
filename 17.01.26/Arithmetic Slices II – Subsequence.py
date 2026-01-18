class Solution:
    def numberOfArithmeticSlices(self, a):
        from collections import defaultdict
        dp=[defaultdict(int) for _ in a]
        r=0
        for i in range(len(a)):
            for j in range(i):
                d=a[i]-a[j]
                c=dp[j][d]
                r+=c
                dp[i][d]+=c+1
        return r
