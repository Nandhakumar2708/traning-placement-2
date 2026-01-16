class Solution(object):
    def isNumber(self, s):
        def integer(n):
            nb=n
            if len(nb)==0 :
                return False       
            if nb[0]=='-' or nb[0]=='+':
                nb=nb[1:]     
            return nb.isdecimal()
        
        def decimal(n):
            nb=n
            F=nb.find('.')
            if len(nb)==0 or F==-1:
                return False       
            if nb[0]=='-' or nb[0]=='+':
                nb=nb[1:] 
                nb=nb[:F-1]+nb[F:]
            else:
                nb=nb[:F]+nb[F+1:]
            return nb.isdecimal()
        
        F=max(s.find('e'),s.find('E'))
        if F==-1 and decimal(s)==False and integer(s)==False:
            return False
        elif F!=-1 and ((decimal(s[:F])==False and integer(s[:F])==False) or integer(s[F+1:])==False):
            return False
        return True
