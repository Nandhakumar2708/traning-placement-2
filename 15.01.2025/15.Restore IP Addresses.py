class Solution(object):
    def helper(self, s, index, result, temp):
        if temp.count('.') == 4:
            if index == len(s):
                result.append(temp[:-1])  
            return

        for length in range(1, 4):
            if index + length > len(s):
                break

            part = s[index:index + length]

            if len(part) > 1 and part[0] == '0':
                continue

            if int(part) > 255:
                continue

            self.helper(s, index + length, result, temp + part + '.')

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.helper(s, 0, result, '')
        return result
