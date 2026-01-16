class Solution(object):
    def reverseBetween(self, head, m, n):
        if m >= n:
            return head
        ohead = dummy = ListNode(0)
        whead = wtail = head
        dummy.next = head
        for i in range(n-m):
            wtail = wtail.next
        for i in range(m-1):
            ohead, whead, wtail = whead, whead.next, wtail.next
        otail, wtail.next = wtail.next, None
        revhead, revtail = self.reverse(whead)
        ohead.next, revtail.next = revhead, otail
        return dummy.next
            
    def reverse(self, head):
        pre, cur, tail = None, head, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail
