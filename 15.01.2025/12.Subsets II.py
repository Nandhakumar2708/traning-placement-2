class Solution(object):
            
    def subsetsWithDup(self, nums):
        nums.sort()
        powerSet = [[]]
        n = len(nums)
        lastAdded = 0
        for i in range(n):
            addingCount =0
            start = 0
            if i>0 and nums[i]==nums[i-1]:
                start = len(powerSet) - lastAdded
            for j in range(start,len(powerSet)):
                arr = powerSet[j]
                newArr = list(arr)
                newArr.append(nums[i])
                powerSet.append(newArr)
                addingCount += 1
            lastAdded = addingCount
        return powerSet
