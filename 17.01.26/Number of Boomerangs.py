class Solution:
    def numberOfBoomerangs(self, p):
        from collections import defaultdict
        r=0
        for i in range(len(p)):
            d=defaultdict(int)
            for j in range(len(p)):
                if i!=j:
                    x=p[i][0]-p[j][0]
                    y=p[i][1]-p[j][1]
                    d[x*x+y*y]+=1
            for v in d.values():
                r+=v*(v-1)
        return r
