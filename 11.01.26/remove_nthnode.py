class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode temp = head;
        while (temp != null) {
            size++;
            temp = temp.next;
        }
        if (n == size) {
            return head.next;
        }
        temp = head;
        int i = 0;
        while (i < size - n - 1) {
            temp = temp.next;
            i++;
        }
        temp.next = temp.next.next;
        return head;
    }
}
