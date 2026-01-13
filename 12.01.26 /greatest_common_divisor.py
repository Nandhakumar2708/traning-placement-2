class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=min(nums)
        n=max(nums)
        gcd=0
        for i in range(1,m+1):
            if m%i==0 and n%i==0:
                gcd=max(gcd,i)
        return gcd



