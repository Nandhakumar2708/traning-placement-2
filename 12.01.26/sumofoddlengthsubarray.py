class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        res = 0
        prefix = [arr[0]]

        for i in range(1 , len(arr)):
            prefix.append(prefix[-1] + arr[i])

        for i in range(len(arr)):
            for j in range(i , len(arr)):
                if (j - i + 1) % 2 == 1:
                    if i == 0:
                        res += prefix[j]
                    else:
                        res += prefix[j] - prefix[i - 1]

        return res
        
