class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        dummyL=ListNode()
        dummyG=ListNode()
        Ltail=dummyL
        Gtail=dummyG
        temp=head
        while temp:
            if temp.val<x:
                Ltail.next=temp
                Ltail=Ltail.next
            else:
                Gtail.next=temp
                Gtail=Gtail.next
            temp=temp.next
        Gtail.next=None
        Ltail.next=dummyG.next
        return dummyL.next
