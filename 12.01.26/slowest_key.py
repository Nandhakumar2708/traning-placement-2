class Solution(object):
    def slowestKey(self, releaseTimes, keysPressed):
        """
        :type releaseTimes: List[int]
        :type keysPressed: str
        :rtype: str
        """
        max_duration = 0
        longest_key = ""

        for i in range(len(keysPressed)):
            if i == 0:
                duration = releaseTimes[0]
            else:
                duration = releaseTimes[i] - releaseTimes[i - 1]
            
            if (duration > max_duration) or (duration == max_duration and keysPressed[i] > longest_key):
                max_duration = duration
                longest_key = keysPressed[i]
        
        return longest_key
                

        
