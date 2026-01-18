class Solution:
    def addTwoNumbers(self, l1, l2):
        s1=[]; s2=[]
        while l1:
            s1.append(l1.val); l1=l1.next
        while l2:
            s2.append(l2.val); l2=l2.next
        c=0; h=None
        while s1 or s2 or c:
            x=s1.pop() if s1 else 0
            y=s2.pop() if s2 else 0
            s=x+y+c
            n=ListNode(s%10)
            n.next=h; h=n
            c=s//10
        return h
