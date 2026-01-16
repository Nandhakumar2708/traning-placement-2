class Solution:
    def deleteDuplicates(self, head):
        dic = {}
        while head!=None:
            if head.val not in dic:
                dic[head.val] = 1
            else:
                dic[head.val] += 1
            head = head.next
        head = None
        for i in dic.keys():
            if dic[i]==1:
                temp = ListNode(i, None)
                if head == None:
                    head = temp
                    prev = temp
                else:
                    prev.next = temp
                    prev = temp
        return head
