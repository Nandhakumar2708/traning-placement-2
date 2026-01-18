class Solution:
    def findMinArrowShots(self, p):
        p.sort(key=lambda x:x[1])
        r=0; e=-10**18
        for s,t in p:
            if s>e:
                r+=1; e=t
        return r
