Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        # 1️⃣ Split list into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # 2️⃣ Sort both halves recursively
        left = self.sortList(head)
        right = self.sortList(mid)

        # 3️⃣ Merge two sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2
        return dummy.next


# 🔍 Helper to convert list to linked list
def create_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# 🔍 Helper to convert linked list to list
def to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


# Test
head = create_list([4,2,1,3])
sol = Solution()
sorted_head = sol.sortList(head)
print(to_list(sorted_head))
