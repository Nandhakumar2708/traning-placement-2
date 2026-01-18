class Solution:
    def deleteNode(self, r, k):
        if not r: return None
        if k<r.val:
            r.left=self.deleteNode(r.left,k)
        elif k>r.val:
            r.right=self.deleteNode(r.right,k)
        else:
            if not r.left: return r.right
            if not r.right: return r.left
            t=r.right
            while t.left: t=t.left
            r.val=t.val
            r.right=self.deleteNode(r.right,t.val)
        return r
