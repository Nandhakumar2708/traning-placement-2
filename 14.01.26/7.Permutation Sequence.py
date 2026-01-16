class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        nums = list(range(1, n+1))
        k -= 1  
        res = []
        for i in range(n, 0, -1):
            fact = math.factorial(i-1)
            index = k // fact
            res.append(str(nums[index]))
            nums.pop(index)
            k %= fact
        return "".join(res)
