class Solution(object):
    def isPrefixString(self, s, words):
        str1 = ""
        n = len(s)
        k = 0
        for items in words:
            str1 += items
            length = len(items)
            k += length
            if k == n:
                break
        if s == str1:
            return True
        else:
            return False
