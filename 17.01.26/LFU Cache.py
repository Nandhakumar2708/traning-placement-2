class LFUCache:
    def __init__(self, c):
        self.c=c; self.kv={}; self.kf={}; self.fk={}
        self.m=0
    def get(self, k):
        if k not in self.kv: return -1
        v,f=self.kv[k]
        self.kf[f].remove(k)
        if not self.kf[f]:
            del self.kf[f]
            if self.m==f: self.m+=1
        self.kf.setdefault(f+1,[]).append(k)
        self.kv[k]=(v,f+1)
        return v
    def put(self, k, v):
        if self.c==0: return
        if k in self.kv:
            self.kv[k]=(v,self.kv[k][1])
            self.get(k); return
        if len(self.kv)==self.c:
            x=self.kf[self.m].pop(0)
            del self.kv[x]
            if not self.kf[self.m]: del self.kf[self.m]
        self.kv[k]=(v,1)
        self.kf.setdefault(1,[]).append(k)
        self.m=1
