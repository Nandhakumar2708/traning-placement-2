class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return str(n)
        counter = 0
        rev = []
        while n > 0:    
            rev.append(str(n%10))
            n = n//10
            counter += 1

            if counter == 3 and n > 0:  # only add '.' if digits are still left
                rev.append('.')
                counter = 0  # reset after dot
        
        thousands = ''.join(list(reversed(rev)))

        return thousands
