class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        dp = [[]] * (n+1) 
        dp[0] = [[]]
        for i in range(1,n+1):
            prev = dp[i-1]
            new_addition = []
            for p in prev: 
                new_addition.append(p+[nums[i-1]])
            dp[i] = prev + new_addition
        return dp[n]
        
