class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Convert binary strings to integers
        sum_int = int(a, 2) + int(b, 2)
        # Convert the integer sum back to a binary string
        # [2:] removes the '0b' prefix added by bin()
        return bin(sum_int)[2:]
        
