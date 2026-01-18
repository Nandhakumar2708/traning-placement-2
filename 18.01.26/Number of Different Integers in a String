class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        l=[]
        s = ""
        for i in word:
            if i.isdigit():
                s=s+i
            if i.isalpha():
                if s !="":
                    l.append(s)
                    s=""
        if s != "":
            l.append(s)

        leading_zeros_l=[]
        for i in l:
            leading_zeros_l.append(int(i))
        ans=set(leading_zeros_l)
        return (len(ans))

        
