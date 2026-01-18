class Solution:
    def sequenceReconstruction(self, o, s):
        from collections import defaultdict,deque
        g=defaultdict(set); d=defaultdict(int)
        for seq in s:
            for i in range(len(seq)-1):
                if seq[i+1] not in g[seq[i]]:
                    g[seq[i]].add(seq[i+1])
                    d[seq[i+1]]+=1
        q=deque([x for x in o if d[x]==0])
        i=0
        while q:
            if len(q)>1: return False
            x=q.popleft()
            if o[i]!=x: return False
            i+=1
            for y in g[x]:
                d[y]-=1
                if d[y]==0:
                    q.append(y)
        return i==len(o)
