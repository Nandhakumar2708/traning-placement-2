class Solution:
    def findDuplicates(self, nums):
        r=[]
        for x in nums:
            i=abs(x)-1
            if nums[i]<0:
                r.append(abs(x))
            nums[i]*=-1
        return r
