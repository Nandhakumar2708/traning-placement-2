class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        for i in range(1,len(nums)):
            if nums[i]>nums[max]:
                max=i
        return max
