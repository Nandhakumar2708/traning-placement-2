class Solution:
    def circularArrayLoop(self, a):
        n=len(a)
        def nxt(i): return (i+a[i])%n
        for i in range(n):
            s=f=i
            d=a[i]>0
            while True:
                s=nxt(s)
                f=nxt(nxt(f))
                if a[s]>0!=d or a[f]>0!=d or a[nxt(f)]>0!=d:
                    break
                if s==f:
                    if s==nxt(s): break
                    return True
        return False
