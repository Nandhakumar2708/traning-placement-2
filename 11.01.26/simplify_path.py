class Solution:
    def simplifyPath(self, path: str) -> str:
        parts=path.split('/')
        k=0
        for part in parts:
            if part=="" or part==".":
                continue
            elif part==".." :
                if k>0:
                    k-=1
            else:
                parts[k]=part
                k+=1
        res="/"+"/".join(parts[:k])
        return res

             
