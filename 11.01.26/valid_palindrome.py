class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned=""
        for ch in s:
            if ch.isalnum():
                cleaned +=ch.lower()
            reversed_string=cleaned[::-1]
        if cleaned==reversed_string:
               return True
        else:
               return False
