class Solution(object):
    def reformatNumber(self, a):
        a = a.replace(" ", "")
        a = a.replace("-", "")
        p = ""
        while len(a) > 0:
            if len(a) > 4 or len(a) == 3:
                p = p + a[0:3] + "-"
                a = a[3:]
            elif len(a) == 2:
                p = p + a[0:2]
                return p
            elif len(a) == 4:
                p = p + a[0:2] + "-" + a[2:]
                return p
        return p[0:len(p)-1]
            

        
