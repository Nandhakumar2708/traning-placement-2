class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (len(nums) == 0):
            return [[]]
        else:
            perms = self.permute(nums[1:])
            out = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p[:]
                    p_copy.insert(i, nums[0])
                    out.append(p_copy)
        return out
