class Solution:
    def compress(self, c):
        i=0; w=0
        while i<len(c):
            j=i
            while j<len(c) and c[j]==c[i]:
                j+=1
            c[w]=c[i]; w+=1
            if j-i>1:
                for x in str(j-i):
                    c[w]=x; w+=1
            i=j
        return w
